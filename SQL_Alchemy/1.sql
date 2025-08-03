SELECT
    p.FirstName,
    p.MiddleName,
    p.LastName,
    e.JobTitle,
    e.HireDate,
    ea.EmailAddress,
    pp.PhoneNumber
FROM
    Person.Person AS p
JOIN
    HumanResources.Employee AS e ON p.BusinessEntityID = e.BusinessEntityID
LEFT JOIN
    Person.EmailAddress AS ea ON p.BusinessEntityID = ea.BusinessEntityID
LEFT JOIN
    Person.PersonPhone AS pp ON p.BusinessEntityID = pp.BusinessEntityID;