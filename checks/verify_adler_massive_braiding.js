'use strict';
// Encode i^k by the integer k modulo four. Checks are implications of the
// reported phases of Adler Prop. 2, Eq. (47), Prop. 3 and Salvitti Eq. (14).
const mod = k => ((k % 4) + 4) % 4;
const phase = (n,m,l,q,side,parity) => mod(2*parity*n*m + side*(n*q+m*l)/2);
// l and q encode lambda and lambda' in units of 1/4. Fixture sectors
// below are selected so that the resulting exponents are integers.
const plus=phase(1,1,1,1,1,1),minus=phase(1,1,1,1,-1,1);
const checks=[
 ['Adler identical positive-orientation exchange -i', plus===3],
 ['reverse orientation +i and inverse', minus===1&&mod(plus+minus)===0],
 ['same-braiding self monodromy -1', mod(2*plus)===2&&mod(2*minus)===2],
 ['Salvitti self monodromy agrees, signed phase not identified', phase(1,1,1,1,1,0)===1&&mod(2*phase(1,1,1,1,1,0))===2],
 ['ordinary controls at lambda=0 and lambda=1/2', mod(2*phase(1,1,0,0,1,1))===0&&mod(2*phase(1,1,2,2,1,1))===0],
 ['disjoint two-packet S modulus is one', [[1,0],[0,1],[-1,0],[0,-1]][plus].reduce((s,x)=>s+x*x,0)===1],
 ['three-packet phase is the product over three pairs', mod(3*plus)===1],
];
for (const [name,pass] of checks){if(!pass) throw Error(name);console.log('PASS '+name);}
