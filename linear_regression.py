temp_c = [7, 13, 19, 24, 43, 8]
temp_f = [44.6, 55.4, 66.2, 75.2, 109.4, 46.4]
w, b = 0, 0
lr = 0.0003
epochs = 1500000
print("-"*10, "Linear Regression by 22davidd", "-"*10)
print(f"epochs: {epochs}")
print(f"learning rate: {lr}")
print("-"*54)
for epoch in range(epochs):
  for i in range(len(temp_c)):
    x = temp_c[i]
    y = temp_f[i]
    pred = w*x+b
    err = y - pred
    dw = -2*err*x
    db = -2*err
    w=w-lr*dw
    b=b-lr*db
print(f"weight: {w}")
print(f"bias: {b}")
print("\n")
print("and the original formula is 9/5+32 which shows we nailed it")
N = 46
print(f"{N} degrees celsius is equal to {(N*w+b):.2f}F for example")
