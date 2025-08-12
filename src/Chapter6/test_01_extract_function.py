from m01_extract_function import process_student_grades


def test_process_student_grades():
    mock_student = {
        "name": "Bob",
        "grades": {
            "Math": 35,
            "Science": 60,
            "History": 57,
            "English": 70,
        },
    }

    expected = {"name": "Bob", "total_score": 222, "average_score": 55.5, "status": "Fail"}

    assert process_student_grades(mock_student) == expected
