def solve_question():
    question = 'Although the content and quality can be as controlled as direct mail, response rates of this medium are lower because of the lack of a personal address mechanism. This media format is known as:'
    options = ['Online banners.', 'Television advertising.', 'Email marketing.', 'Care lines.', 'Direct mail.', 'Inserts.', 'Door to door.', 'Radio advertising.', 'Billboards.', 'Social media advertising.']
    correct_answer = 'Direct mail.'
    for option in options:
        if option == correct_answer:
            print('The correct answer is:', option)
            print('Returning answer:', option)
            print(option)
            return option

print(solve_question())