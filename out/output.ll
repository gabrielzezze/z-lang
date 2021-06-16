; ModuleID = "/home/gabrielzezze/Desktop/Insper/LogiComp/z-lang/src/Codegen/CodeGen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define i8 @"main"() 
{
entry:
  %".2" = bitcast [5 x i8]* @"fstr" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", [64 x i8] c"'aq'                                                            ")
  %".4" = call i8 @"printer"([64 x i8] c"'aq'                                                            ")
  ret i8 0
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%i \0a\00"
define i8 @"printer"([64 x i8] %".1") 
{
func_printer_entry:
  %"frase" = alloca [64 x i8]
  store [64 x i8] %".1", [64 x i8]* %"frase"
  %"frase.1" = load [64 x i8], [64 x i8]* %"frase"
  %".4" = bitcast [5 x i8]* @"fstr" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", [64 x i8] %"frase.1")
  %"x" = alloca i8
  store i8 0, i8* %"x"
  %"x.1" = load i8, i8* %"x"
  %".7" = icmp slt i8 %"x.1", 6
  br i1 %".7", label %"while_6c444603_f584_4129_a5cf_8fd21c66be71", label %"exit_while_6c444603_f584_4129_a5cf_8fd21c66be71"
while_6c444603_f584_4129_a5cf_8fd21c66be71:
  %"x.2" = load i8, i8* %"x"
  %".9" = add i8 %"x.2", 2
  store i8 %".9", i8* %"x"
  %"x.3" = load i8, i8* %"x"
  %".11" = bitcast [5 x i8]* @"fstr" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i8 %"x.3")
  %"x.4" = load i8, i8* %"x"
  %".13" = icmp slt i8 %"x.4", 6
  br i1 %".13", label %"while_6c444603_f584_4129_a5cf_8fd21c66be71", label %"exit_while_6c444603_f584_4129_a5cf_8fd21c66be71"
exit_while_6c444603_f584_4129_a5cf_8fd21c66be71:
  ret i8 0
}
