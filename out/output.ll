; ModuleID = "/home/gabrielzezze/Desktop/Insper/LogiComp/z-lang/src/Codegen/CodeGen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define i8 @"main"() 
{
entry:
  %"x" = alloca i8
  store i8 2, i8* %"x"
  %".3" = bitcast [5 x i8]* @"fstr" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", [11 x i8] c"'Pre While'")
  %"x.1" = load i8, i8* %"x"
  %".5" = icmp slt i8 %"x.1", 6
  br i1 %".5", label %"while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b", label %"exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b"
while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b:
  %"x.2" = load i8, i8* %"x"
  %".7" = call i8 @"add_2"(i8 %"x.2")
  store i8 %".7", i8* %"x"
  %"x.3" = load i8, i8* %"x"
  %".9" = icmp slt i8 %"x.3", 6
  br i1 %".9", label %"while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b", label %"exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b"
exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b:
  %"x.4" = load i8, i8* %"x"
  %".11" = call i8 @"add_2"(i8 %"x.4")
  %".12" = sub i8 %".11", 2
  %".13" = bitcast [5 x i8]* @"fstr" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i8 %".12")
  %"x.5" = load i8, i8* %"x"
  %".15" = icmp eq i8 %"x.5", 5
  br i1 %".15", label %"exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b.if", label %"exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b.else"
exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b.if:
  %".17" = bitcast [5 x i8]* @"fstr" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i8 10)
  br label %"exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b.endif"
exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b.else:
  %"x.6" = load i8, i8* %"x"
  %"x.7" = load i8, i8* %"x"
  %".20" = call i8 @"add_2"(i8 %"x.7")
  %".21" = sub i8 %".20", 2
  %".22" = icmp sgt i8 %"x.6", %".21"
  br i1 %".22", label %"exit_while_1012060f_d1eb_...if", label %"exit_while_1012060f_d1eb_...else"
exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b.endif:
  %"y" = alloca [6 x i8]
  store [6 x i8] c"'AQUI'", [6 x i8]* %"y"
  %"y.1" = alloca [8 x i8]
  store [8 x i8] c"'AQUI 2'", [8 x i8]* %"y.1"
  %"x.8" = load i8, i8* %"x"
  %".33" = bitcast [5 x i8]* @"fstr" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", i8 %"x.8")
  %"x.9" = load i8, i8* %"x"
  %"x.10" = load i8, i8* %"x"
  %".35" = call i8 @"sub"(i8 %"x.9", i8 %"x.10")
  %".36" = bitcast [5 x i8]* @"fstr" to i8*
  %".37" = call i32 (i8*, ...) @"printf"(i8* %".36", i8 %".35")
  ret i8 0
exit_while_1012060f_d1eb_...if:
  %".24" = bitcast [5 x i8]* @"fstr" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i8 12)
  br label %"exit_while_1012060f_d1eb_...endif"
exit_while_1012060f_d1eb_...else:
  %".27" = bitcast [5 x i8]* @"fstr" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i8 11)
  br label %"exit_while_1012060f_d1eb_...endif"
exit_while_1012060f_d1eb_...endif:
  br label %"exit_while_1012060f_d1eb_4d1f_b57b_96e90b64ad0b.endif"
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%i \0a\00"
define i8 @"add_2"(i8 %".1") 
{
func_add_2_entry:
  %"y" = alloca i8
  store i8 %".1", i8* %"y"
  %"y.1" = load i8, i8* %"y"
  %".4" = bitcast [5 x i8]* @"fstr" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8 %"y.1")
  %"y.2" = load i8, i8* %"y"
  %".6" = add i8 %"y.2", 2
  ret i8 %".6"
}

define i8 @"sub"(i8 %".1", i8 %".2") 
{
func_sub_entry:
  %"h" = alloca i8
  store i8 %".1", i8* %"h"
  %"e" = alloca i8
  store i8 %".2", i8* %"e"
  %"h.1" = load i8, i8* %"h"
  %"e.1" = load i8, i8* %"e"
  %".6" = sub i8 %"h.1", %"e.1"
  ret i8 %".6"
}
