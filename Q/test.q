0N!"Testing";
a:1;
lookback:1000*29;
while [a<=3600;
	ctable:a#table;
	ctime:last ctable[`time];
	company:last ctable[`sym];
	/window:select avg price by sym from ctable where time within (ctime-lookback;ctime);
	window:select avg price,sym from ctable where (sym=`A) & (time within (ctime-lookback;ctime));
	/0N!window;
	/0N!(string[.z.t], " pA: ",.Q.f[4;window[`A][`price]], " pB: ",.Q.f[4;window[`B][`price]], " pC: ",.Q.f[4;window[`C][`price]], " pD: ",.Q.f[4;window[`D][`price]]);
	if [company=`A;0N!(string[.z.t], " pA: ",.Q.f[4;window[`price][0]])];
	/system "sleep 1";
	a:a+1;];
0N!"Done!"
