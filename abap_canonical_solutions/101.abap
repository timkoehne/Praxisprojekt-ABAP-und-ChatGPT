FUNCTION Z_WORDS_STRING.
*"----------------------------------------------------------------------
*"*"Local Interface:
*"  IMPORTING
*"     VALUE(INPUT_STRING) TYPE  STRING
*"  EXPORTING
*"     VALUE(OUTPUT_TABLE) TYPE  STRINGTAB
*"----------------------------------------------------------------------

  SPLIT input_string AT ',' INTO TABLE output_table.

ENDFUNCTION.