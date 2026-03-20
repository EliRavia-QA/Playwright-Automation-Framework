import allure
import json


class TestAPI:
    @allure.title("בדיקת API - שליפת פוסטים")
    def test_get_posts_api(self, api_only):
        with allure.step("שליחת בקשת GET לשרת"):
            response = api_only.api_request.get("/posts")
            response_json = response.json()

        with allure.step("אימות סטטוס ותוכן התשובה"):
            assert response.status == 200

            allure.attach(
                json.dumps(response_json, indent=4),  # הופך את ה-JSON לטקסט קריא עם רווחים
                name="Response Body",
                attachment_type=allure.attachment_type.JSON
            )

            assert len(response_json) > 0

    @allure.title("בדיקת API - יצירת פוסט חדש (POST)")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_post_api(self, api_only):

        new_post_data = {
            "title": "Automation is Awesome",
            "body": "Learning API testing with Playwright and Allure",
            "userId": 1
        }

        with allure.step("שליחת בקשת POST עם נתוני הפוסט החדש"):

            allure.attach(
                json.dumps(new_post_data, indent=4),
                name="Request Payload (Data Sent)",
                attachment_type=allure.attachment_type.JSON
            )


            response = api_only.api_request.post("/posts", data=new_post_data)

        with allure.step("אימות יצירת הפוסט"):

            assert response.status == 201, f"Expected 201 but got {response.status}"

            response_json = response.json()


            allure.attach(
                json.dumps(response_json, indent=4),
                name="Response Body (Data Received)",
                attachment_type=allure.attachment_type.JSON
            )

            assert response_json["title"] == new_post_data["title"]
            assert "id" in response_json, "Server did not return a new ID"
            print(f"Created post with ID: {response_json['id']}")