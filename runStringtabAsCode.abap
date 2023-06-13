
REPORT Z_XM_DEVXM_277_PPTEST.

DATA: PROGNAME TYPE PROGRAM.
DATA: MSG TYPE STRING.
DATA: LIN TYPE I.
DATA: WRD TYPE STRING.
DATA: OFF TYPE I.
DATA: MID TYPE TRMSG_KEY.
DATA: SID TYPE STRING.
DATA FINISH TYPE STRINGTAB.
DATA CURRENT TYPE STRING.
DATA COUNTER TYPE I.

DATA MNAME TYPE STRING. "method name
DATA RNAME TYPE STRING. "return value line
DATA CLASSMETHOD TYPE STRING. "new line for class Methods definition

DATA FIRSTWORD TYPE STRING.

DATA(IT_CODE) = VALUE STRINGTAB( ( |PROGRAM SUBPOOL.| )
                                 ( |CLASS main DEFINITION.| )
                                 ( |  PUBLIC SECTION.| )
                                 ( |    CLASS-METHODS show| )
                                 ( |      RETURNING VALUE(ret_val) TYPE string.| )
                                 ( |ENDCLASS.| )
                                 ( |CLASS main IMPLEMENTATION.| )
                                 ( |  METHOD show.| )
                                 ( |    WRITE: 'test'.| )
                                 ( |    ret_val = \|\{ 'test' \} - Return value.\|.| )
                                 ( |  ENDMETHOD.| )
                                 ( |ENDCLASS.| ) ).

DATA(TEST) = VALUE STRINGTAB( ( | METHOD isPalindrome.                                                          | )
                              ( |   RETURNING VALUE(rv_is_palindrome) TYPE abap_bool.                           | )
                              ( |   DATA: lv_input_string TYPE string,                                          | )
                              ( |         lv_reversed_string TYPE string,                                       | )
                              ( |         lv_length TYPE i,                                                     | )
                              ( |         lv_index TYPE i.                                                      | )
                              ( |                                                                               | )
                              ( |   lv_input_string = iv_input_string.                                          | )
                              ( |   lv_length = strlen( lv_input_string ).                                      | )
                              ( |                                                                               | )
                              ( |   DO lv_length TIMES.                                                         | )
                              ( |     lv_index = lv_length - sy-index + 1.                                      | )
                              ( |     lv_reversed_string = lv_reversed_string && lv_input_string+lv_index(1).   | )
                              ( |   ENDDO.                                                                      | )
                              ( |                                                                               | )
                              ( |   rv_is_palindrome = ( lv_input_string = lv_reversed_string ).                | )
                              ( | ENDMETHOD.                                                                    | ) ).

*DATA(TEST) = VALUE STRINGTAB( ( | METHOD ispalin.                                                              | )
*                              ( |   RETURNING VALUE(RET_VAL) TYPE i.                                           | )
*                              ( |   RET_VAL = 1.                                                               | )
*                              ( | ENDMETHOD.                                                                   | ) ).


* find method name
WRITE: 'Extrahiere relevante Daten: '.
NEW-LINE.
READ TABLE TEST INTO MNAME INDEX 1.
CONDENSE MNAME.
MNAME = CONDENSE( VAL = MNAME DEL = '.' ).
SPLIT MNAME AT SPACE INTO FIRSTWORD MNAME.
NEW-LINE.
WRITE: 'methodname: ', MNAME.
NEW-LINE.

* find returnvalue name
READ TABLE TEST INTO RNAME INDEX 2.
CONDENSE RNAME.
WRITE: 'returnvalue: ', RNAME.
NEW-PAGE.

* build new program code
LOOP AT IT_CODE INTO CURRENT.
  CONDENSE CURRENT.
  IF COUNTER = 3.
    CONCATENATE 'CLASS-METHODS ' MNAME INTO CLASSMETHOD RESPECTING BLANKS.
    APPEND CLASSMETHOD TO FINISH.
  ELSEIF COUNTER = 4.
    APPEND RNAME TO FINISH.
  ELSEIF COUNTER >= 7.
    EXIT.
  ELSE.
    APPEND CURRENT TO FINISH.
  ENDIF.
  COUNTER = COUNTER + 1.
ENDLOOP.

COUNTER = 0.
LOOP AT TEST INTO CURRENT.
  IF COUNTER <> 1.
    CONDENSE CURRENT.
    APPEND CURRENT TO FINISH.
  ENDIF.
  COUNTER = COUNTER + 1.
ENDLOOP.

APPEND 'ENDCLASS.' TO FINISH.

WRITE: 'Zusammengesetzter Programmcode: '.
NEW-LINE.
LOOP AT FINISH INTO CURRENT.
  WRITE CURRENT.
  NEW-LINE.
ENDLOOP.

NEW-PAGE.

* Subroutinen-Pool im ABAP-Speicher des akt. Programms erzeugen
* finish wird übergeben, Programmname wird temporär vom System vergeben
GENERATE SUBROUTINE POOL FINISH
  NAME PROGNAME
  MESSAGE MSG
  LINE LIN
  WORD WRD
  OFFSET OFF
  MESSAGE-ID MID
  SHORTDUMP-ID SID.

CASE SY-SUBRC.
  WHEN 0. " ok
    TRY.
* dynamischen Klassennamen ermitteln
        DATA(LV_CLASS) = |\\PROGRAM={ PROGNAME }\\CLASS=MAIN|.
        DATA: RET TYPE STRING.

* statischer Methodenaufruf
        TRANSLATE MNAME TO UPPER CASE.

        CALL METHOD (LV_CLASS)=>(MNAME)
          RECEIVING
            RET_VAL = RET.

        WRITE: 'Rückgabewert: '.
        NEW-LINE.
        WRITE: / RET.

      CATCH CX_ROOT INTO DATA(E_TEXT).
        WRITE: 'Fehlermeldung im Try-Catch:'.
        NEW-LINE.
        WRITE E_TEXT->GET_TEXT( ).
    ENDTRY.

  WHEN 4. " Syntaxfehler
    WRITE: 'Fehlermeldung Syntaxfehler:'.
    NEW-LINE.
    WRITE MSG.
  WHEN 8. " Laufzeitfehler
    WRITE: 'Fehlermeldung Laufzeitfehler:'.
    NEW-LINE.
    WRITE SID.
  WHEN OTHERS.
    WRITE: 'Fehlermeldung:'.
    NEW-LINE.
    WRITE: / 'Unbekannter Fehler'.
ENDCASE.