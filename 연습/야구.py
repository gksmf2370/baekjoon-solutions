import random

def generate_number():
    # 서로 다른 네 자리 숫자를 생성
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]

def get_user_guess():
    while True:
        guess = input("네 자리 숫자를 입력하세요: ")
        if len(guess) != 4 or not guess.isdigit():
            print("유효한 네 자리 숫자를 입력하세요.")
        else:
            return [int(d) for d in guess]

def calculate_score(secret, guess):
    strikes = 0
    balls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            strikes += 1
        elif guess[i] in secret:
            balls += 1
    return strikes, balls

def print_decorated_message(message):
    decoration = '*' * (len(message) + 4)
    print(decoration)
    print(f"* {message} *")
    print(decoration)

def main():
    secret_number = generate_number()
    attempts = 0
    print_decorated_message("숫자 야구 게임에 오신 것을 환영합니다!")
    
    while True:
        guess = get_user_guess()
        attempts += 1
        strikes, balls = calculate_score(secret_number, guess)
        
        print_decorated_message(f"{strikes} 스트라이크, {balls} 볼")
        
        if strikes == 4:
            print_decorated_message(f"축하합니다! {attempts}번 만에 맞추셨습니다.")
            break

if __name__ == "__main__":
    main()
