# Online_Exam

** Users should register first , then they get their token and should use it to get questions.
   They get 5 random questions and after that should pass their answer , Then they get their result.

** A brief view over project's URLs :




   1.register/ ==> user should register by json like this : {"username" : "Negar" , "password" : "1234" , "address" : "Tehran"}
   2.questions/ ==> for get random questions.Users should send their token key in request's header like this :
                    Authorization : Token fa5b2ec21eae949b5df32a52afeff761ccc39c14
   3.ans/ ==> Users should send their answers by json in a way that key is the number of question and value is the selected 
              choice , like this : {"1" : " 2" , "16" : " 3" , "20" : " 1"}
   
