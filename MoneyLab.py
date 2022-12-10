Program prim_10_5;
Var   n,k,x:word;
Begin
  Write('Введите число'); Readln(n);
  K:=64;
  While n>0 do
  Begin
    If n>=k then begin Writeln(n div k, 'купюр по ', k);n:=n mod k end;
    K:=k div 2
  End;
  Readln
End.
