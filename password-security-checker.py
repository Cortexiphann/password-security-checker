#FurkanFilikci
def rate_password(password):
    score = 0

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    special_characters = "!@#$%^&*()-_=+[]{};:,.<>/?`~"
    if any(c in special_characters for c in password):
        score += 1

    return score

def evaluate_password_security(password):
    security_score = rate_password(password)

    if security_score <= 1:
        return "Parola güvensiz. Daha karmaşık bir parola seçin."
    elif security_score == 2:
        return "Parola zayıf bir güvenlik seviyesine sahip. Daha karmaşık bir parola seçmeyi düşünebilirsiniz."
    elif security_score == 3:
        return "Parola orta düzeyde bir güvenlik seviyesine sahip."
    elif security_score == 4:
        return "Parola iyi bir güvenlik seviyesine sahip."
    else:
        return "Parola güvenli."

password = input("Parolanızı girin: ")

result = evaluate_password_security(password)
print(result)
