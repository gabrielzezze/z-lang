; ModuleID = "/home/gabrielzezze/Desktop/Insper/LogiComp/z-lang/src/Codegen/CodeGen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define i8 @"main"() 
{
entry:
  %"x" = alloca i8
  store i8 2, i8* %"x"
  %"x.1" = load i8, i8* %"x"
  %".3" = icmp slt i8 %"x.1", 6
  br i1 %".3", label %"while_b1676017_8831_46e1_a151_9acb7ca94143", label %"exit_while_b1676017_8831_46e1_a151_9acb7ca94143"
while_b1676017_8831_46e1_a151_9acb7ca94143:
  %"x.2" = load i8, i8* %"x"
  %".5" = call i8 @"add_2"(i8 %"x.2")
  store i8 %".5", i8* %"x"
  %"x.3" = load i8, i8* %"x"
  %".7" = icmp slt i8 %"x.3", 6
  br i1 %".7", label %"while_b1676017_8831_46e1_a151_9acb7ca94143", label %"exit_while_b1676017_8831_46e1_a151_9acb7ca94143"
exit_while_b1676017_8831_46e1_a151_9acb7ca94143:
  %"x.4" = load i8, i8* %"x"
  %".9" = bitcast [5 x i8]* @"fstr" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i8 %"x.4")
  ret i8 0
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%i \0a\00"
define i8 @"add_2"(i8 %".1") 
{
func_add_2_entry:
  %"x" = alloca i8
  store i8 %".1", i8* %"x"
  %"x.1" = load i8, i8* %"x"
  %".4" = bitcast [5 x i8]* @"fstr" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8 %"x.1")
  %"x.2" = load i8, i8* %"x"
  %".6" = add i8 %"x.2", 2
  ret i8 %".6"
}
