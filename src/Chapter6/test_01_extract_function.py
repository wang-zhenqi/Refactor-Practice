from m01_extract_function import process_student_grades


def test_process_student_grades():
    mock_student = {
        "name": "Bob",
        "grades": {
            "Math": 35,
            "Science": 60,
            "History": 57,
            "English": 90,
        },
    }

    expected = {"name": "Bob", "total_score": 242, "average_score": 60.5, "status": "Pass"}

    assert process_student_grades(mock_student) == expected
