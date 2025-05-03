import os
from flask_backend.app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
@app.route("/")
def health():
    return "OK", 200
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import json
# import os

# app = Flask(__name__)
# CORS(app)  # فعال‌سازی CORS

# TASKS_FILE = "tasks.json"

# # 📌 تابع برای خواندن کارها از فایل (با بررسی فایل خالی)
# def load_tasks():
#     if not os.path.exists(TASKS_FILE):  # بررسی وجود فایل
#         return []
#     try:
#         with open(TASKS_FILE, "r") as file:
#             return json.load(file)
#     except json.JSONDecodeError:
#         return []

# # 📌 تابع برای ذخیره کارها در فایل
# def save_tasks(tasks):
#     with open(TASKS_FILE, "w") as file:
#         json.dump(tasks, file, indent=4)

# # 📌 دریافت لیست کارها
# @app.route("/tasks", methods=["GET"])
# def get_tasks():
#     tasks = load_tasks()
#     return jsonify(tasks)

# # 📌 اضافه کردن کار جدید
# @app.route("/tasks", methods=["POST"])
# def add_task():
#     tasks = load_tasks()
#     data = request.json

#     new_task = {
#         "id": len(tasks) + 1 if tasks else 1,  # ساختن ID جدید
#         "title": data.get("title", "تسک بدون نام"),
#         "done": data.get("done", False)  # پیش‌فرض انجام نشده
#     }

#     tasks.append(new_task)
#     save_tasks(tasks)
#     return jsonify(new_task), 201  # ارسال تسک جدید

# # 📌 ویرایش کار
# @app.route("/tasks/<int:task_id>", methods=["PUT"])
# def update_task(task_id):
#     tasks = load_tasks()
#     for task in tasks:
#         if task["id"] == task_id:
#             data = request.json
#             task["title"] = data.get("title", task["title"])
#             task["done"] = data.get("done", task["done"])
#             save_tasks(tasks)
#             return jsonify(task), 200
#     return jsonify({"error": "Task not found"}), 404

# # 📌 حذف کار
# @app.route("/tasks/<int:task_id>", methods=["DELETE"])
# def delete_task(task_id):
#     tasks = load_tasks()
#     new_tasks = [task for task in tasks if task["id"] != task_id]

#     if len(new_tasks) == len(tasks):
#         return jsonify({"error": "Task not found"}), 404

#     save_tasks(new_tasks)
#     return jsonify({"message": "Task deleted"}), 200

# # 📌 تغییر ترتیب تسک‌ها
# @app.route("/reorder-tasks", methods=["PUT"])
# def reorder_tasks():
#     data = request.json
#     if "tasks" not in data:
#         return jsonify({"error": "Invalid data"}), 400
    
#     tasks = data["tasks"]
#     save_tasks(tasks)
#     return jsonify({"message": "Tasks reordered successfully"}), 200

# if __name__ == "__main__":
#     app.run(debug=True)
