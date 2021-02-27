N:3600;
times:09:30:00.0000+1000*til N;
idx:N?4;
syms:`A`B`C`D idx;
pxs:(1+N?0.1)*200 100 150 300 idx;
table:([] time:times;sym:syms;price:pxs);
