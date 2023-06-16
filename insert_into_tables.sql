INSERT INTO departments (name)
VALUES
('Sales department'),
('Legal department'),
('Development department'),
('Marketing department');


INSERT INTO employees (username, email, hashed_password, phone_number, first_name, last_name, start_date, department_id)
VALUES
('user1', 'user1@example.com', '$2b$12$TneSu2WKhbVsxngEowynS.dWNwMC/sFPThtoyvbA6zMuO7UqHkJ9C', '+11111111111', 'User1', 'Name1', '2022-01-01', 3),
('user2', 'user2@example.com', '$2b$12$H6JJQPfTHayBoyrju11d1uo04qNfus7OJmDVYANW4e3LVthgBr3uG', '+22222222222', 'User2', 'Name2', '2022-02-02', 3),
('user3', 'user3@example.com', '$2b$12$QHAStr.hHxsQSsm696rR1Ow4LS0X9ydgfFngFxzqvan.SQ6LYWj8q', '+33333333333', 'User3', 'Name3', '2022-03-03', 1),
('user4', 'user4@example.com', '$2b$12$UtjBvBmZD2vfAzSpgDqnjun4N4W97nJYkPrC83w.Y57XB0HkMgaeO', '+44444444444', 'User4', 'Name4', '2022-04-04', 1),
('user5', 'user5@example.com', '$2b$12$hm0qaT3bbe3PDgwAqLYScuXQvYAUi96RqQ/RsTxnLtVxmMRmD/sBS', '+55555555555', 'User5', 'Name5', '2022-05-05', 2),
('user6', 'user6@example.com', '$2b$12$fQI7y2ErqKcV9g/cvv8MwuRA53RIAwnKgDugjkmRmiyI4HR.jvYPu', '+66666666666', 'User6', 'Name6', '2022-06-06', 2),
('user7', 'user7@example.com', '$2b$12$fQI7y2ErqKcV9g/cvv8MwuRA53RIAwnKgDugjkmRmiyI4HR.jvYPu', '+77777777777', 'User7', 'Name7', '2022-07-07', 4),
('user8', 'user8@example.com', '$2b$12$nLlEKT5tn0L5xW1KDSWABOQ0p03kXY7Wygf21oZpHtNmIU6krcs82', '+88888888888', 'User8', 'Name8', '2022-08-08', 4);



INSERT INTO salaries (employee_id, department_id, current_salary, next_salary, raise_date)
VALUES
(1, 3, 50000.00, 60000.00, '2022-07-01'),
(2, 3, 50000.00, 60000.00, '2022-08-02'),
(3, 1, 50000.00, 60000.00, '2022-09-03'),
(4, 1, 50000.00, 60000.00, '2022-10-04'),
(5, 2, 50000.00, 60000.00, '2022-11-05'),
(6, 2, 50000.00, 60000.00, '2022-12-06'),
(7, 4, 50000.00, 60000.00, '2023-01-07'),
(8, 4, 50000.00, 60000.00, '2023-02-08');
-- 5 user Password.4