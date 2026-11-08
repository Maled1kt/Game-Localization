# Game Localization

![Banner Game Localization dengan dua panel dialog gim yang bertukar karakter dari berbagai bahasa](../assets/game-localization-banner.png)

[English](../README.md) · [Semua bahasa](../README.md#languages)

Game Localization adalah skill agen untuk menerjemahkan, menyunting, dan meninjau teks gim di ChatGPT, Codex, dan Claude. Skill ini mencakup menu, tutorial, dialog, takarir, teks toko, dan dokumentasi proyek untuk Steam, PlayStation, Xbox, serta gim seluler.

[Pemasangan](#pemasangan) · [Menggunakan skill](#menggunakan-skill) · [Memperbarui atau menghapus](#memperbarui-atau-menghapus) · [Dukung pembuat](#dukung-pembuat) · [Rencana pengembangan](../ROADMAP.md) · [Riwayat perubahan](../CHANGELOG.md)

## Fitur

- Menerapkan istilah proyek yang disetujui dan mencatat istilah baru sebagai usulan.
- Mempertahankan kunci pelokalan, placeholder seperti `{player_name}` dan `%s`, tag, pemisah baris yang bermakna, dan elemen lain yang dilindungi.
- Memeriksa batas panjang dan memisahkan terjemahan dari pertanyaan, koreksi sumber, dan catatan pemeriksaan kualitas.
- Menyediakan [daftar bawaan 30 bahasa dan varian](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) serta mendukung daftar kustom.
- Menyertakan [glosarium awal 75 istilah dalam 30 bahasa dan varian](../game-localization/references/glossary/README.md) dengan definisi bersama dalam bahasa Inggris dan usulan terjemahan.

Skill berisi petunjuk dan berkas rujukan. Skill ini berjalan tanpa kunci API proyek, konektor, atau layanan latar belakang. Penyuntingan berkas bergantung pada alat di chat. Sebelum rilis, periksa UI di build gim dan teks toko di pratinjau platform.

## Pemasangan

| Lingkungan | Paket |
| --- | --- |
| ChatGPT atau Codex dengan izin unggah plugin | [ZIP plugin ChatGPT](../packages/game-localization-chatgpt-v0.1.6.zip) |
| Claude atau ruang kerja ChatGPT yang mengizinkan unggah skill mandiri | [ZIP skill mandiri](../packages/game-localization-skill-v0.1.6.zip) |
| Codex lokal atau Claude Code | [Pasang dari folder sumber](#pemasangan-lokal-dengan-satu-perintah) |

Buka tautan paket di GitHub dan pilih **Download raw file**. Unggah ZIP tanpa mengekstraknya.

### ChatGPT dan Codex

1. Di ChatGPT versi web, buka opsi unggah plugin akun Anda. Pemilik dan administrator ruang kerja yang berwenang dapat menggunakan **Admin console → Plugins → Add → Upload plugin**.
2. Pilih ZIP plugin. Setelah validasi, buka **Game Localization** di **Plugins** dan pilih **Install plugin** jika tersedia. Unggahan pribadi dapat muncul di **Personal → Created by me**.
3. Buka chat baru di ChatGPT atau Codex. Ketik `@` dan pilih **Game Localization** dari saran.

Jika ruang kerja mendukung skill mandiri, buka **Plugins → Skills → Create → Upload from your computer** dan unggah ZIP skill mandiri. Tunggu pemindaian dan ikuti petunjuk. Pilihan bergantung pada akun dan ruang kerja. [Panduan plugin OpenAI](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Panduan skill OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Aktifkan **Code execution and file creation** di pengaturan Claude jika akun atau ruang kerja mensyaratkannya.
2. Di Claude versi web atau Claude Desktop, buka **Customize → Skills**. Di tampilan baru, buka **Plugins** dari bilah samping dan cari pengelolaan skill di **Your plugins**.
3. Pilih **+ → Create skill → Upload a skill** dan unggah ZIP mandiri. Aktifkan `game-localization` setelah muncul.
4. Mulai chat baru dan minta Claude memakai **Game Localization**. Jika skill muncul di menu **+** atau **/** pada kolom pesan, pilih di sana.

Di ruang kerja terkelola, administrator mungkin harus mengaktifkan atau mengunggah skill. [Panduan skill Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Bilah samping baru Claude](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Pemasangan lokal dengan satu perintah

Perintah di bawah memakai cabang `main` dari [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Perintah dapat digunakan setelah repositori dan cabang dipublikasikan. Tautan ZIP relatif juga berfungsi pada cabang, tag, dan fork lain.

Di chat Codex lokal, pilih `$skill-installer` bawaan dan kirim permintaan berikut. Izinkan akses jaringan jika diminta, lalu mulai sesi baru. [Panduan skill Codex](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Skills CLI pihak ketiga memasang folder sumber yang sama untuk Codex lokal dan Claude Code dalam satu perintah. Jalankan dari proyek tujuan dengan Node.js 22.20 atau lebih baru. Sisakan opsi `-a` untuk agen yang dibutuhkan. Tambahkan `-g` untuk memasang bagi pengguna saat ini di semua proyek. [Referensi Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Di chat terminal Claude Code lokal, gunakan input shell untuk memasang khusus ke Claude. Periksa URL repositori sebelum menjalankan perintah. [Input shell Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Dalam sesi baru, panggil `$game-localization` di Codex atau `/game-localization` di Claude Code. Untuk pemasangan manual, salin seluruh folder `game-localization/` ke `.claude/skills/` proyek atau `~/.claude/skills/` pengguna. [Panduan skill Claude Code](https://code.claude.com/docs/en/skills)

Pada ChatGPT dan Claude yang dihosting, gunakan fitur unggah atau pasang pada akun. Penyebutan di chat memanggil skill yang terpasang. Untuk membagikan tautan, publikasikan melalui direktori yang didukung platform atau bagikan skill maupun plugin di ruang kerja yang memenuhi syarat. [Berbagi plugin ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Berbagi skill Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Menggunakan skill

1. Lampirkan teks atau berkas sumber dan glosarium proyek terbaru untuk bahasa sasaran. Jika belum ada glosarium, minta draf secara eksplisit.
2. Tentukan bahasa sumber dan sasaran, platform, jenis materi, dan format hasil. Sertakan batas karakter, tangkapan layar, keterangan penutur, atau contoh variabel jika perlu.
3. Untuk lembar kerja, sebutkan kolom sumber dan sasaran serta minta salinan baru. Untuk string gim, berikan ID atau kunci tetap. Untuk toko, tentukan kolom tujuan dan batas panjang wajib jika ada.
4. Baca laporan penyerahan terpisah untuk mengetahui apakah hasilnya siap digunakan atau masih berupa draf. Laporan itu memisahkan pemeriksaan file, tinjauan bahasa, dan pemeriksaan dalam game atau pratinjau toko, serta mencantumkan langkah berikutnya untuk setiap masalah yang belum selesai. Setujui istilah di glosarium proyek sebelum menggunakannya kembali.

**Contoh permintaan untuk lembar kerja**

~~~text
Gunakan Game Localization untuk menerjemahkan kolom ENGLISH di buku kerja terlampir ke bahasa Jerman (de-DE). Masukkan terjemahan ke GERMAN dalam salinan .xlsx baru. Gunakan glosarium terlampir dan kolom DESCRIPTION sebagai konteks. Pertahankan kunci, kolom sumber, placeholder, dan tag. Cantumkan pertanyaan istilah dan hasil pemeriksaan secara terpisah beserta ID baris.
~~~

**Contoh permintaan untuk halaman toko**

~~~text
Gunakan Game Localization untuk melokalkan deskripsi singkat Steam ini dari bahasa Inggris ke bahasa Portugis Brasil (pt-BR). Buat draf glosarium jika diperlukan. Pertahankan judul gim dan patuhi batas karakter yang ditentukan. Berikan teks toko dan laporan penyerahan secara terpisah.
~~~

### Memeriksa terjemahan CSV

Jika CSV memiliki ID baris yang tetap, sebutkan judul kolom ID, teks sumber, dan terjemahan. Jika Python 3.9 atau versi yang lebih baru tersedia, skill membandingkan file sumber dengan file terjemahan dan menandai ID yang hilang atau ganda, terjemahan kosong, perubahan pada placeholder atau tag yang didukung, dan teks yang melebihi batas panjang. [Petunjuk pemeriksaan CSV](../game-localization/references/csv-qa.md)

Coba [contoh penggunaan pertama dengan 12 baris](../game-localization/examples/first-run/README.md) yang mencakup draf terjemahan, glosarium yang sudah disetujui, dan contoh laporan penyerahan.

### Setelan model kami

| Lingkungan | Model | Tingkat penalaran |
| --- | --- | --- |
| ChatGPT Work atau Codex | GPT-6.1 Sol | High atau lebih tinggi jika tersedia |
| Claude | Claude Opus 5.5 | High atau lebih tinggi jika tersedia |

**High+** berarti High atau tingkat lebih tinggi yang tersedia di aplikasi. Pilih model dan tingkat penalaran di aplikasi. Skill berjalan terlepas dari pengaturan ini. [Pengaturan model OpenAI](https://learn.chatgpt.com/docs/models) · [Tingkat penalaran Claude](https://platform.claude.com/docs/en/build-with-claude/effort)

## Memperbarui atau menghapus

| Pemasangan | Perbarui | Hapus |
| --- | --- | --- |
| Plugin ChatGPT atau Codex | Jika Anda mengelola unggahan, pilih **Upload new version** pada detail plugin. Pemasangan dari direktori atau ruang kerja menerima pembaruan dari sumbernya. | Buka **Plugins → Installed → Game Localization** dan pilih **Uninstall plugin** jika tersedia. Tanyakan kepada administrator untuk pemasangan terkelola. |
| Skill mandiri ChatGPT | Ganti unggahan pribadi dengan ZIP mandiri terbaru melalui pengelola skill. | Buka **Plugins → Skills**, cari di **Installed** atau **Created by me**, lalu gunakan opsi penghapusan. Administrator mengelola skill milik ruang kerja. |
| Skill kustom Claude | Unggah ZIP mandiri baru dari halaman pengelolaan. Nonaktifkan versi lama jika muncul entri kedua. | Buka skill di **Customize → Skills** atau **Plugins** lalu nonaktifkan. Untuk unggahan Anda, pilih **⋯ → Delete** dan konfirmasi. |
| Skill lokal dari Skills CLI | Untuk cabang yang dilacak, jalankan `npx skills update game-localization` atau pasang dari tag terbaru. | Jalankan `npx skills remove game-localization` di proyek yang sama. Tambahkan `-g` jika dipasang secara global. |
| Folder lokal atau Codex Skill Installer | Ganti folder `game-localization/` dengan versi terbaru. | Hapus folder `game-localization/`. Codex dapat memuatnya dari `.agents/skills/`, `~/.agents/skills/`, atau `~/.codex/skills/`. Claude Code memakai `.claude/skills/` atau `~/.claude/skills/`. Mulai sesi baru bila perlu. |

[Pengelolaan plugin OpenAI](https://learn.chatgpt.com/docs/plugins) · [Pengelolaan skill kustom Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Kode sumber dan paket

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) menentukan kapan skill digunakan dan cara memproses sekumpulan teks.
- [`game-localization/references/`](../game-localization/references/) berisi aturan dan edisi glosarium awal per bahasa.
- [`packaging/chatgpt/`](../packaging/chatgpt/) berisi manifes dan ikon plugin.
- [`packages/`](../packages/) berisi arsip yang siap diunggah.

Untuk membangun ulang kedua ZIP dari sumber yang sama, jalankan `python scripts/package.py` dari akar repositori dengan Python 3.9 atau lebih baru. Versi berasal dari manifes plugin ChatGPT. Sebelum mendistribusikan, unggah tiap ZIP ke produk tujuannya dan uji dengan sedikit teks yang memuat glosarium dan placeholder terlindungi.

## Lisensi

Game Localization tersedia dengan [Lisensi MIT](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Dukung pembuat

Jika Game Localization membantu tim Anda, Anda dapat [mendukung Maled1kt melalui DonationAlerts](https://www.donationalerts.com/r/maled1kt). Donasi sepenuhnya sukarela.
