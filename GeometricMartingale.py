def run_signal_generator():
    print("--- Xgenium : trading signal tool ---")
    
    # Initial Configuration
    total_capital = float(input("Enter total capital (e.g. 1000): "))
    entry_price = float(input("Enter your INITIAL entry price: "))
    current_price = float(input("Enter CURRENT market price: "))
    
    # Martingale Steps (n + n + 2n + 4n...)
    # index 0 is first buy, index 1 is first drop, etc.
    sequence = [0.1, 0.1, 0.2, 0.4, 0.8] # percentage of capital deployed in strategy, compared to net capital
    
    # For this simple script, we assume user is on Step 0 (The first 10%)
    step = int(input("Which step are you on? (0 for first buy, 1 for first drop, etc.): "))
    
    # Calculate price change %
    change = (current_price - entry_price) / entry_price
    
    print(f"\nStatus: Price is {change:+.2%}")
    
    # Logic Engine
    if change >= 0.03:
        print(">>> SIGNAL: SELL INSTANTLY (Target Hit)")
        print(f"Action: Sell position and bank the profit. Reset to Step 0.")
        
    elif change <= -0.05:
        next_step = step + 1
        if next_step < len(sequence):
            required_capital = total_capital * sequence[next_step]
            print(f">>> SIGNAL: BUY - DROPPED 5% (Martingale Step {next_step})")
            print(f"Action: Deploy {sequence[next_step]*100}% of capital (£{required_capital}).")
        else:
            print(">>> SIGNAL: HOLD/STOP - Sequence limit reached.")
            
    else:
        print(">>> SIGNAL: NO ACTION (Waiting for +3% or -5%)")
        print(f"Current P/L: £{ (total_capital * sequence[step]) * change :.2f}")

if __name__ == "__main__":
    run_signal_generator()
