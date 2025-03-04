 The attendance data set contains two types of fixed-width files.  
 
 ATTENDANCE. The attendance files represents the D2L output for a single quiz that was used to track attendance.  
 Students retook this same quiz each day at the start of class, so the number of attempts for a student corresponds to
 their total attendance on that date, and the maximum of each student's attempt # is the total attendance for said student
 that semester. Note that all scores should be 1 out of 1, as it is impossible to get the one question wrong.  This means that
 the Score, Out of, and Percent columns are not meaningful here.

 PRACTICE.  The attendance files represents the D2L output for a given modules multiple choice (MC) practice quiz.
 These quizzes can be attempted an unlimited number of times and students are encourage to take them until they feel prepared for the
 module's actual MC quiz.  In this case, the Score, Out of, and Percent columns are meaningful, as they track the student's progress.

 COLUMN NAME [WIDTH]   DESCRIPTION
 Org Defined ID [9]    Unique student ID
 UserName [9]          starID
 FirstName [12]        Student's first name
 LastName [12]         Student's last name
 Attempt # [3]         Quiz attempt number (represents total attendance on that date for an attendance file)
 Score [3]             Score (should always be 1 for an attendance file)
 Out Of [3]            Maximum possible points (should be 1 for an attendance file)
 Attempt_Start [20]    date-time for the start of the quiz
 Attempt_End [20]      date-time for the end of the quiz
 Percent [6]           Percent of total points (100*Score/Out of)