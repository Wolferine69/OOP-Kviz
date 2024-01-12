import data
import question_model
import quiz_brain 

list_otazek=[]

for one_question in data.question_data:
    new_question=question_model.Question(one_question["text"],one_question["answer"])
    list_otazek.append(new_question)

kviz=quiz_brain.QuizBrain(list_otazek)

while kviz.has_questions():
    kviz.next_question()

print(f"Dosahl jste na skore {kviz.skore} / {kviz.question_number}")