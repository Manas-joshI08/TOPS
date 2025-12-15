-- Active: 1757520973560@@localhost@3306@try
CREATE DATABASE try;
USE try;
DROP TABLE employees;
CREATE TABLE employees (
  employee_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  position VARCHAR(100),
  salary DECIMAL(10,2),
  hire_date DATE
);
drop TABLE employee_audit;
CREATE TABLE employee_audit (
  audit_id INT AUTO_INCREMENT PRIMARY KEY,
  employee_id INT,
  name VARCHAR(100),
  position VARCHAR(100),
  salary DECIMAL(10,2),
  hire_date DATE,
  action_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DELIMITER $$

CREATE TRIGGER after_employee_insert
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
  INSERT INTO employee_audit (employee_id, name, position, salary, hire_date)
  VALUES (NEW.employee_id, NEW.name, NEW.position, NEW.salary, NEW.hire_date);
END $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS add_employee;
CREATE PROCEDURE add_employee(
  IN p_name VARCHAR(100),
  IN p_position VARCHAR(100),
  IN p_salary DECIMAL(10,2),
  IN p_hire_date DATE
)
BEGIN
  INSERT INTO employees (name, position, salary, hire_date)
  VALUES (p_name, p_position, p_salary, p_hire_date);
END $$

DELIMITER ;

CALL add_employee('Ravi Patel', 'Tester', 55000, '2024-05-01');

SELECT * FROM employee_audit;

DELETE FROM employees
ORDER BY employee_id DESC
LIMIT 2;

SELECT * FROM employee_audit;