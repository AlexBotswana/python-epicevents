-- Insert records into the Clients table
INSERT INTO Customers (firstname, lastname, email, phone, company_name, located, creation_date, last_contact_date, commercial_user_id) VALUES
('Kevin', 'Casey', 'kevin@startup.io', '+678 123 456 78', 'Cool Startup LLC', 'Paris', '2021-04-18', '2023-03-29', 3),
('John', 'Ouick', 'john.ouick@gmail.com', '+1 234 567 8901', 'Some Company', 'New York', '2022-06-10', '2023-06-28', 3),
('Lou', 'Bouzin', 'lou@bouzin.com', '+ 666 12345', 'Lou Bouzin Inc.', 'London', '2023-01-15', '2024-02-20', 5);

-- Insert records into the Contracts table
INSERT INTO Contracts (customer_id, commercial_user_id, title, total_amount, remaining_amount, creation_date, statement_id) VALUES
(1, 2, 'Sales Contract 2023', 5000.00, 2000.00, '2023-05-15', 1),
(2, 3, 'Service Agreement 2022', 8000.00, 6000.00, '2022-10-20', 3),
(3, 1, 'Renewal Contract 2024', 3000.00, 3000.00, '2024-01-05', 2),
(3, 2, 'Cancelled Contract 2023', 10000.00, 1000.00, '2024-01-06', 4);

-- Insert records into the Events table
INSERT INTO Events (contract_id, title, begin_date, end_date, support_user_id, located, attendees, notes) VALUES
(1, 'Annual Sales Conference', '2023-06-10 09:00:00', '2023-06-12 17:00:00', 4, 'Paris Expo Center', 100, 'Keynote speaker: Jack Smith'),
(2, 'Product Launch Event', '2022-11-30 18:00:00', '2022-11-30 22:00:00', 4, 'Grand Central Hall', 200, 'Demo booths will be set up'),
(3, 'Client Appreciation Dinner', '2024-02-25 19:00:00', '2024-02-25 22:00:00', 6, 'Lou Bouzin Inc. Headquarters', 50, 'Catering by Gourmet Delights');
