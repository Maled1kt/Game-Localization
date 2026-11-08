# Game Localization

![Ảnh bìa Game Localization với hai khung thoại trong trò chơi trao đổi ký tự từ nhiều ngôn ngữ](../assets/game-localization-banner.png)

[English](../README.md) · [Tất cả ngôn ngữ](../README.md#languages)

Game Localization là kỹ năng dành cho tác nhân để dịch, biên tập và rà soát văn bản trò chơi trong ChatGPT, Codex và Claude. Kỹ năng hỗ trợ menu, hướng dẫn, lời thoại, phụ đề, nội dung cửa hàng và tài liệu dự án cho Steam, PlayStation, Xbox và trò chơi di động.

[Cài đặt](#cài-đặt) · [Sử dụng kỹ năng](#sử-dụng-kỹ-năng) · [Cập nhật hoặc gỡ bỏ](#cập-nhật-hoặc-gỡ-bỏ) · [Ủng hộ tác giả](#ủng-hộ-tác-giả) · [Kế hoạch phát triển](../ROADMAP.md) · [Nhật ký thay đổi](../CHANGELOG.md)

## Tính năng

- Áp dụng thuật ngữ đã duyệt của dự án và ghi lại thuật ngữ mới dưới dạng đề xuất.
- Giữ nguyên khóa bản địa hóa, biến giữ chỗ như `{player_name}` và `%s`, thẻ, ngắt dòng có ý nghĩa và các phần tử được bảo vệ khác.
- Kiểm tra giới hạn độ dài và tách bản dịch khỏi câu hỏi, phần sửa nguyên bản và ghi chú kiểm tra chất lượng.
- Cung cấp [danh sách mặc định gồm 30 ngôn ngữ và biến thể](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) và chấp nhận danh sách tùy chỉnh.
- Có [bảng thuật ngữ khởi đầu gồm 75 mục cho cả 30 ngôn ngữ và biến thể](../game-localization/references/glossary/README.md), với định nghĩa chung bằng tiếng Anh và bản dịch đề xuất.

Kỹ năng gồm hướng dẫn và tệp tham chiếu. Kỹ năng hoạt động mà không cần khóa API dự án, trình kết nối hay dịch vụ nền. Việc chỉnh sửa tệp tùy vào công cụ trong cuộc trò chuyện. Trước khi phát hành, hãy kiểm tra giao diện trong bản dựng trò chơi và nội dung cửa hàng trong bản xem trước của nền tảng.

## Cài đặt

| Môi trường | Gói |
| --- | --- |
| ChatGPT hoặc Codex có quyền tải plugin lên | [ZIP plugin ChatGPT](../packages/game-localization-chatgpt-v0.1.4.zip) |
| Claude hoặc không gian ChatGPT được phép tải kỹ năng độc lập lên | [ZIP kỹ năng độc lập](../packages/game-localization-skill-v0.1.4.zip) |
| Codex cục bộ hoặc Claude Code | [Cài từ thư mục nguồn](#cài-cho-tác-nhân-cục-bộ-bằng-một-lệnh) |

Mở liên kết gói trên GitHub và chọn **Download raw file**. Tải lên nguyên tệp ZIP.

### ChatGPT và Codex

1. Trong ChatGPT trên web, mở mục tải plugin lên của tài khoản. Chủ sở hữu và quản trị viên có quyền có thể dùng **Admin console → Plugins → Add → Upload plugin**.
2. Chọn ZIP plugin. Sau khi xác thực, mở **Game Localization** trong **Plugins** và chọn **Install plugin** nếu có. Bản tải lên cá nhân có thể xuất hiện trong **Personal → Created by me**.
3. Mở cuộc trò chuyện mới trong ChatGPT hoặc Codex. Nhập `@` và chọn **Game Localization** từ danh sách gợi ý.

Nếu không gian hỗ trợ kỹ năng độc lập, dùng **Plugins → Skills → Create → Upload from your computer** để tải ZIP tương ứng lên. Chờ quét và làm theo hướng dẫn. Tùy chọn phụ thuộc vào tài khoản và không gian làm việc. [Hướng dẫn plugin OpenAI](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Hướng dẫn kỹ năng OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Bật **Code execution and file creation** trong cài đặt Claude nếu tài khoản hoặc không gian yêu cầu.
2. Trong Claude trên web hoặc Claude Desktop, mở **Customize → Skills**. Với giao diện mới, mở **Plugins** ở thanh bên và tìm mục quản lý kỹ năng trong **Your plugins**.
3. Chọn **+ → Create skill → Upload a skill** rồi chọn ZIP độc lập. Bật `game-localization` khi xuất hiện.
4. Mở cuộc trò chuyện mới và yêu cầu Claude dùng **Game Localization**. Nếu kỹ năng hiện trong mục **+** hoặc **/** ở ô nhập, hãy chọn tại đó.

Trong không gian được quản lý, quản trị viên có thể phải bật hoặc tải kỹ năng lên. [Hướng dẫn kỹ năng Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Thanh bên mới của Claude](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Cài cho tác nhân cục bộ bằng một lệnh

Các lệnh dưới đây dùng nhánh `main` của [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Có thể chạy sau khi kho mã và nhánh được công bố. Liên kết ZIP tương đối cũng dùng được trên nhánh, thẻ và fork khác.

Trong cuộc trò chuyện Codex cục bộ, chọn `$skill-installer` có sẵn và gửi yêu cầu bên dưới. Cho phép truy cập mạng nếu được hỏi rồi mở phiên mới. [Hướng dẫn kỹ năng Codex](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Skills CLI của bên thứ ba cài cùng thư mục nguồn cho Codex cục bộ và Claude Code bằng một lệnh. Dùng Node.js 22.20 trở lên và chạy trong dự án đích. Chỉ giữ tùy chọn `-a` cho tác nhân cần cài. Thêm `-g` để cài ở cấp người dùng. [Tham khảo Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Trong cuộc trò chuyện terminal của Claude Code cục bộ, dùng ô nhập shell để cài riêng cho Claude. Kiểm tra URL kho mã trước khi chạy. [Nhập lệnh shell trong Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Trong phiên mới, gọi `$game-localization` trong Codex hoặc `/game-localization` trong Claude Code. Để cài thủ công, sao chép toàn bộ thư mục `game-localization/` vào `.claude/skills/` của dự án hoặc `~/.claude/skills/` của người dùng. [Hướng dẫn kỹ năng Claude Code](https://code.claude.com/docs/en/skills)

Trên ChatGPT và Claude trực tuyến, dùng chức năng tải lên hoặc cài đặt của tài khoản. Nhắc tên trong cuộc trò chuyện sẽ gọi kỹ năng đã cài. Để có liên kết cài đặt chia sẻ được, hãy phát hành qua danh mục được nền tảng hỗ trợ hoặc chia sẻ kỹ năng hay plugin trong không gian đủ điều kiện. [Chia sẻ plugin ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Chia sẻ kỹ năng Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Sử dụng kỹ năng

1. Đính kèm văn bản hoặc tệp nguồn và bảng thuật ngữ hiện hành cho ngôn ngữ đích. Nếu chưa có bảng thuật ngữ, hãy yêu cầu soạn bản nháp.
2. Nêu ngôn ngữ nguồn và đích, nền tảng, loại nội dung và định dạng đầu ra. Thêm giới hạn ký tự, ảnh chụp, ghi chú về người nói hoặc ví dụ về biến khi cần.
3. Với bảng tính, nêu tên cột nguồn và cột đích rồi yêu cầu tạo bản sao. Với chuỗi trong trò chơi, cung cấp khóa hoặc ID ổn định. Với nội dung cửa hàng, nêu trường đích và giới hạn bắt buộc nếu có.
4. Xem các dòng còn vướng, thuật ngữ tạm thời và các kiểm tra đã hoàn tất trong báo cáo bàn giao. Duyệt thuật ngữ trước khi dùng lại, rồi kiểm tra bản dịch trong bản dựng hoặc bản xem trước của cửa hàng.

**Ví dụ câu lệnh cho bảng tính**

~~~text
Dùng Game Localization để dịch cột ENGLISH trong sổ làm việc đính kèm sang tiếng Đức (de-DE). Ghi bản dịch vào cột GERMAN của bản sao .xlsx mới. Tham khảo bảng thuật ngữ đính kèm và cột DESCRIPTION. Giữ nguyên khóa, cột nguồn, biến giữ chỗ và thẻ. Liệt kê riêng câu hỏi thuật ngữ và kết quả kiểm tra kèm ID dòng.
~~~

**Ví dụ câu lệnh cho trang cửa hàng**

~~~text
Dùng Game Localization để bản địa hóa mô tả ngắn Steam này từ tiếng Anh sang tiếng Bồ Đào Nha Brazil (pt-BR). Soạn bảng thuật ngữ nháp nếu cần. Giữ nguyên tên trò chơi và tuân thủ giới hạn ký tự đã cho. Trả nội dung cửa hàng và báo cáo bàn giao riêng.
~~~

### Kiểm tra bản dịch trong CSV

Nếu tệp CSV có ID cố định cho từng dòng, hãy nêu tên các cột chứa ID, văn bản nguồn và bản dịch. Khi có Python 3.9 trở lên, kỹ năng sẽ so sánh tệp nguồn với tệp đã dịch và báo các ID bị thiếu hoặc trùng, bản dịch để trống, thay đổi ở biến giữ chỗ hoặc thẻ được hỗ trợ và trường hợp vượt giới hạn độ dài. [Hướng dẫn kiểm tra CSV](../game-localization/references/csv-qa.md)

### Thiết lập mô hình của chúng tôi

| Môi trường | Mô hình | Mức suy luận |
| --- | --- | --- |
| ChatGPT Work hoặc Codex | GPT-6.1 Sol | High trở lên, nếu có |
| Claude | Claude Opus 5.5 | High trở lên, nếu có |

**High+** là cách gọi tắt mức High hoặc cao hơn trong ứng dụng. Chọn mô hình và mức suy luận trong ứng dụng. Kỹ năng hoạt động độc lập với lựa chọn này. [Thiết lập mô hình OpenAI](https://learn.chatgpt.com/docs/models) · [Mức suy luận của Claude](https://platform.claude.com/docs/en/build-with-claude/effort)

## Cập nhật hoặc gỡ bỏ

| Cách cài đặt | Cập nhật | Gỡ bỏ |
| --- | --- | --- |
| Plugin ChatGPT hoặc Codex | Nếu bạn quản lý bản tải lên, chọn **Upload new version** ở trang chi tiết. Bản cài từ danh mục hoặc không gian làm việc nhận cập nhật từ nguồn đó. | Mở **Plugins → Installed → Game Localization** và chọn **Uninstall plugin** nếu có. Hỏi quản trị viên về bản cài được quản lý. |
| Kỹ năng ChatGPT độc lập | Dùng trang quản lý để thay bản tải lên cá nhân bằng ZIP độc lập mới nhất. | Mở **Plugins → Skills**, tìm trong **Installed** hoặc **Created by me** và chọn gỡ bỏ nếu có. Quản trị viên quản lý kỹ năng thuộc không gian. |
| Kỹ năng tùy chỉnh Claude | Tải ZIP độc lập mới lên trang quản lý. Tắt bản cũ nếu xuất hiện mục thứ hai. | Mở trong **Customize → Skills** hoặc **Plugins** rồi tắt. Với bản bạn đã tải lên, chọn **⋯ → Delete** và xác nhận. |
| Kỹ năng cục bộ cài bằng Skills CLI | Chạy `npx skills update game-localization` nếu đang theo dõi một nhánh hoặc cài từ thẻ mới. | Chạy `npx skills remove game-localization` trong cùng dự án. Thêm `-g` nếu đã cài toàn cục. |
| Thư mục cục bộ hoặc Codex Skill Installer | Thay thư mục `game-localization/` đã cài bằng phiên bản mới nhất. | Xóa thư mục `game-localization/`. Codex có thể nạp từ `.agents/skills/`, `~/.agents/skills/` hoặc `~/.codex/skills/`. Claude Code dùng `.claude/skills/` hoặc `~/.claude/skills/`. Mở phiên mới nếu cần. |

[Quản lý plugin OpenAI](https://learn.chatgpt.com/docs/plugins) · [Quản lý kỹ năng tùy chỉnh Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Mã nguồn và đóng gói

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) quy định khi nào kỹ năng chạy và cách xử lý một lô văn bản.
- [`game-localization/references/`](../game-localization/references/) chứa quy tắc và các bảng thuật ngữ theo ngôn ngữ.
- [`packaging/chatgpt/`](../packaging/chatgpt/) chứa tệp kê khai và biểu tượng plugin.
- [`packages/`](../packages/) chứa các tệp nén sẵn để tải lên.

Để tạo lại hai ZIP từ cùng nguồn, chạy `python scripts/package.py` ở thư mục gốc kho mã với Python 3.9 trở lên. Phiên bản lấy từ tệp kê khai plugin ChatGPT. Trước khi phân phối, tải từng ZIP lên đúng sản phẩm và thử một lô nhỏ có bảng thuật ngữ và biến giữ chỗ được bảo vệ.

## Giấy phép

Game Localization được phát hành theo [giấy phép MIT](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Ủng hộ tác giả

Nếu Game Localization hữu ích cho nhóm của bạn, hãy cân nhắc [ủng hộ Maled1kt qua DonationAlerts](https://www.donationalerts.com/r/maled1kt). Việc ủng hộ hoàn toàn tự nguyện.
