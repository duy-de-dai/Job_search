import json
import os

class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file_path = 'db/data.json'
        self.file = None

    def close_spider(self, spider):
        # Đóng file sau khi crawl kết thúc
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        if not self.file:
            self.file_exists = os.path.isfile(self.file_path)
            self.file = open(self.file_path, 'w', encoding='utf-8')
            
            # Kiểm tra xem file đã tồn tại chưa
            if self.file_exists:
                # Mở file và đọc nội dung
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Nếu file không rỗng và kết thúc bằng "]", thì xóa dấu "]"
                if content and content.endswith("]"):
                    content = content[:-1]
                    # Ghi lại nội dung đã được chỉnh sửa
                    self.file.write(content)

        # Kiểm tra xem file đã rỗng hay không tồn tại để đặt dấu "[" và loại bỏ dấu ","
        if not self.file_exists or (self.file_exists and not content):
            self.file.write("[")

        line = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line + ",\n")
        return item
