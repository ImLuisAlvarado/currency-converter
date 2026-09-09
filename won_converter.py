def mxn_to_krw(amount_mxn, exchange_rate=79.0):
    krw_amount = amount_mxn * exchange_rate

    print("\n" + "=" * 30)
    print(f"  MXN:  ${amount_mxn:,.2f}")
    print(f"  KRW:  ₩{krw_amount:,.2f}")
    print("=" * 30)

    return krw_amount