num_rounds = int(input())
score = 0
final_score = 0
i = 0
for i in range (0,num_rounds):
    score = float(input())
    if score > 100:
        score = score + (score * 0.20)
    final_score = final_score + score

rounds_processed = num_rounds
print(f"{final_score:.1f}")
print(rounds_processed)
