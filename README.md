# GeometricMartingaleStrategy
An open source project that uses a Dollar Cost Averaging strategy using a geometric martingale style system for retail trading and investing. 

Xgenium is developing a stack of trading tools, this algorithm is popular amongst retail trading, now made into code to be deployed as an automated signal generator.

The martingale strategy is a stochastic process which focuses on probabilisitc returns in trading (and gambling), by DCA, your overall exposure increases, whilst your average price decreases. 

Be careful of the sunk cost fallacy where using this strategy in trading, you are throwing money into dying positions. trade and gamble responsibly and learn from the martingale in both its upside and downside potentials. 

Users should be aware of the Negative Skewness: while the probability of small wins is high, the "tail risk" involves a total capital wipeout if the asset undergoes a permanent impairment of value.

The strategy is defined by the growth of the position size:
Initial Move (n): 10% of Total Capital.
Scaling Factor: 2^x (after the initial buffer).
Risk Profile: This is a Finite Martingale. Unlike a theoretical infinite martingale, our strategy is constrained by the "Gambler's Ruin" (the point where total capital equals 0 and no further steps can be taken).
