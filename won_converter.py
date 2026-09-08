def mxn_to_krw(exchange_rate=72.0):
    try:
        mxn_amount = float(input("Enter amount in Mexican Pesos (MXN): "))
        krw_amount = mxn_amount * exchange_rate

        print("\n" + "=" * 30)
        print(f"  MXN:  ${mxn_amount:,.2f}")
        print(f"  KRW:  ₩{krw_amount:,.2f}")
        print("=" * 30)
    except ValueError:
        print("\nError: Please enter a valid numerical value.")




