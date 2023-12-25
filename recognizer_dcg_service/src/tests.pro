:-include('rules_english.pro').
:-include('rules_simple.pro').

:- s(Tree, [terry,writes,a,program,that,halts],[]), 
   Tree = s(np(pn(terry)),
            vp(tv(writes),
               np(det(a),
                  n(program),
                  rel(that,
                      vp(iv(halts)))))).
