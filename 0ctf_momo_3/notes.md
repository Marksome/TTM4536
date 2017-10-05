mov    cx,WORD PTR ds:0x81fe6f2 #eax+ecx=ebx
mov    DWORD PTR ds:0x81fe6f0,edx #matematikk, inn i edx
mov    ds:0x8055740,eax #flyttes inn i eax
mov    eax,DWORD PTR [eax*4+0x81aa170] #får begge tall
mov    al,BYTE PTR [eax+edx*1] #noe morro
0x805356e:   mov    eax,0x8055723
0x8053573:   mov    ds:0x805574c,eax # Congratulations
0x8053732:   cmp    DWORD PTR ds:0x83fe848,0x1
0x8053739:   je     0x8048290 <puts@plt>
