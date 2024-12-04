
# RESTful API Todo List 練習

這是一個基於 **Python Django** 與 **Django REST Framework (DRF)** 的練習專案，用於構建一個簡單的 RESTful API 來管理 Todo List。目的是熟悉 RESTful API 的基礎概念和操作，包括 CRUD（Create, Read, Update, Delete）功能。

---

## 專案功能

- **新增任務**：使用 `POST` 方法新增一個待辦事項。
- **查看任務列表**：使用 `GET` 方法檢視所有待辦事項。
- **查看單一任務**：使用 `GET` 方法查看特定任務的詳細內容。
- **更新任務**：使用 `PUT` 或 `PATCH` 方法更新任務內容。
- **刪除任務**：使用 `DELETE` 方法刪除特定任務。

---

## 環境需求

- Python 3.8+
- Django 4.x
- Django REST Framework 3.x

---


6. **測試 API**
   在瀏覽器或 API 工具（如 Postman、Thunder Client）中訪問：
   - API 總覽列表：`http://127.0.0.1:8000/api/todos/`
   - 單一任務操作：`http://127.0.0.1:8000/api/todos/<id>/`

---

## API 文件

### 任務資源

| 方法  | URL                        | 說明             |
|-------|----------------------------|------------------|
| GET   | `/api/todos/`              | 獲取所有任務     |
| POST  | `/api/todos/`              | 新增任務         |
| GET   | `/api/todos/<id>/`         | 獲取特定任務     |
| PUT   | `/api/todos/<id>/`         | 更新特定任務     |
| PATCH | `/api/todos/<id>/`         | 部分更新特定任務 |
| DELETE| `/api/todos/<id>/`         | 刪除特定任務     |

### 範例資料格式

**新增任務**
```json
POST /api/todos/
{
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs",
    "completed": false
}
```

**更新任務**
```json
PUT /api/todos/1/
{
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs, Butter",
    "completed": true
}
```


## 技術重點

1. **Django REST Framework**
   - 使用 `ModelViewSet` 簡化 CRUD 實作。
   - 使用序列化器（Serializers）處理資料序列化與驗證。
2. **RESTful API 設計**
   - 遵守 RESTful 架構風格，使用統一資源定位（URI）與方法（GET、POST、PUT、DELETE）。
3. **SQLite 資料庫**
   - 使用 Django 預設的 SQLite 作為開發環境資料庫。
4. **測試**
   - 可透過 Postman、Thunder Client 或 cURL 測試 API 功能。

---

