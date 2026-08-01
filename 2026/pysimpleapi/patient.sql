-- =========================
-- Patients Table
-- =========================
CREATE TABLE Patients (
    PatientID SERIAL PRIMARY KEY,
    RegisteredBy VARCHAR(10) NOT NULL,

    MRN VARCHAR(50) NOT NULL UNIQUE,
    FullName VARCHAR(100) NOT NULL,
    DOB DATE NOT NULL,
    ICNum VARCHAR(20) NOT NULL,
    Barcode VARCHAR(100) NOT NULL,
    RegisteredTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    LastUpdated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT FK_Patients_User
        FOREIGN KEY (RegisteredBy)
        REFERENCES Users(UserID)
);