; ModuleID = "/home/gabrielzezze/Desktop/Insper/LogiComp/z-lang/src/Codegen/CodeGen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = alloca i8
  store i8 2, i8* %".2"
  %".4" = load i8, i8* %".2"
  %".5" = icmp slt i8 %".4", 6
  br i1 %".5", label %"while_eaf03562_71cf_4f18_b671_d2a81b0fff1e", label %"exit_while_eaf03562_71cf_4f18_b671_d2a81b0fff1e"
while_eaf03562_71cf_4f18_b671_d2a81b0fff1e:
  %".7" = load i8, i8* %".2"
  %".8" = add i8 %".7", 2
  store i8 %".8", i8* %".2"
  %".10" = load i8, i8* %".2"
  %".11" = bitcast [5 x i8]* @"fstr" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i8 %".10")
  %".13" = load i8, i8* %".2"
  %".14" = icmp slt i8 %".13", 6
  br i1 %".14", label %"while_eaf03562_71cf_4f18_b671_d2a81b0fff1e", label %"exit_while_eaf03562_71cf_4f18_b671_d2a81b0fff1e"
exit_while_eaf03562_71cf_4f18_b671_d2a81b0fff1e:
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%i \0a\00"