# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [Tüm diller](../README.md#languages)

Game Localization, ChatGPT, Codex ve Claude’da oyun metinlerini çevirmek, düzenlemek ve incelemek için kullanılan bir ajan becerisidir. Steam, PlayStation, Xbox ve mobil oyunlar için menüleri, eğitimleri, diyalogları, altyazıları, mağaza metinlerini ve proje belgelerini kapsar.

[Kurulum](#kurulum) · [Beceriyi kullanma](#beceriyi-kullanma) · [Güncelleme veya kaldırma](#güncelleme-veya-kaldırma) · [Geliştiriciyi destekleyin](#geliştiriciyi-destekleyin) · [Geliştirme planı](../ROADMAP.md) · [Değişiklik günlüğü](../CHANGELOG.md)

## Özellikler

- Projenin onaylı terminolojisini uygular ve yeni terimleri öneri olarak kaydeder.
- Yerelleştirme anahtarlarını, `{player_name}` ve `%s` gibi yer tutucuları, etiketleri, anlamlı satır sonlarını ve korunan diğer öğeleri muhafaza eder.
- Belirtilen uzunluk sınırlarını kontrol eder. Çevirileri sorulardan, kaynak düzeltmelerinden ve kalite kontrolü notlarından ayrı tutar.
- [30 dil ve dil varyantından oluşan bir hazır liste](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) sunar ve özel listeleri kabul eder.
- Ortak İngilizce tanımları ve çeviri önerilerini içeren, [30 dil ve varyantın tamamında 75 terimlik başlangıç sözlüğü](../game-localization/references/glossary/README.md) sunar.

Beceri, yönergeler ve başvuru dosyaları içerir. Proje API anahtarı, bağlayıcı veya arka plan hizmeti gerektirmez. Dosya düzenleme olanağı sohbetteki araçlara bağlıdır. Yayımlamadan önce çevrilmiş arayüzü oyun derlemesinde, mağaza metnini de platformun önizlemesinde kontrol edin.

## Kurulum

| Ortam | Paket |
| --- | --- |
| Eklenti yükleme yetkisi olan ChatGPT veya Codex | [ChatGPT eklentisi ZIP dosyası](../packages/game-localization-chatgpt-v0.1.10.zip) |
| Claude veya bağımsız beceri yükleyebilen ChatGPT çalışma alanları | [Bağımsız beceri ZIP dosyası](../packages/game-localization-skill-v0.1.10.zip) |
| Yerel Codex veya Claude Code | [Kaynak klasörden kurulum](#yerel-ajanlar-için-tek-komutla-kurulum) |

GitHub’da paket bağlantısını açıp **Download raw file** seçeneğini seçin. ZIP dosyasını açmadan yükleyin.

### ChatGPT ve Codex

1. Web’deki ChatGPT’de hesabın eklenti yükleme seçeneğini açın. Yetkili çalışma alanı sahipleri ve yöneticiler **Admin console → Plugins → Add → Upload plugin** yolunu kullanabilir.
2. Eklenti ZIP’ini seçin. Doğrulamadan sonra **Plugins** bölümünde **Game Localization** öğesini açıp varsa **Install plugin** seçeneğini seçin. Kişisel yüklemeler **Personal → Created by me** altında görünebilir.
3. ChatGPT veya Codex’te yeni sohbet açın. `@` yazıp önerilerden **Game Localization** öğesini seçin.

Çalışma alanı bağımsız becerileri destekliyorsa **Plugins → Skills → Create → Upload from your computer** yolundan bağımsız beceri ZIP’ini yükleyin. Taramanın bitmesini bekleyip yönergeleri izleyin. Seçenekler hesaba ve çalışma alanına bağlıdır. [OpenAI eklenti kılavuzu](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI beceri kılavuzu](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Hesap veya çalışma alanı gerektiriyorsa Claude ayarlarından **Code execution and file creation** seçeneğini açın.
2. Web’deki Claude’da veya Claude Desktop’ta **Customize → Skills** bölümünü açın. Yeni düzende kenar çubuğundaki **Plugins** bölümüne gidip **Your plugins** altındaki beceri ayarlarını bulun.
3. **+ → Create skill → Upload a skill** yolundan bağımsız ZIP’i seçin. Göründüğünde `game-localization` becerisini etkinleştirin.
4. Yeni sohbet açıp Claude’dan **Game Localization** kullanmasını isteyin. Beceri, yazma alanındaki **+** veya **/** menüsünde görünüyorsa oradan seçin.

Yönetilen çalışma alanlarında beceriyi bir yöneticinin etkinleştirmesi veya yüklemesi gerekebilir. [Claude beceri kılavuzu](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Claude’un yeni kenar çubuğu](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Yerel ajanlar için tek komutla kurulum

Komutlar [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization) deposunun `main` dalını kullanır. Depo ve dal yayımlandığında çalışırlar. Göreli ZIP bağlantıları başka dallarda, etiketlerde ve çatallarda da çalışır.

Yerel Codex sohbetinde yerleşik `$skill-installer` aracını seçip aşağıdaki isteği gönderin. Gerekirse ağ erişimine izin verip yeni oturum başlatın. [Codex beceri kılavuzu](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Üçüncü taraf Skills CLI, yerel Codex ve Claude Code için aynı kaynak klasörü tek terminal komutuyla kurabilir. Hedef projede Node.js 22.20 veya üstüyle çalıştırın. Yalnızca gereken ajanların `-a` seçeneklerini bırakın. Kullanıcı genelinde kurmak için `-g` ekleyin. [Skills CLI başvuru belgesi](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Yerel Claude Code terminal sohbetinde yalnızca Claude için kurulum yapmak üzere kabuk girişini kullanın. Çalıştırmadan önce depo URL’sini kontrol edin. [Claude Code kabuk girişi](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Yeni oturumda Codex’te `$game-localization` veya Claude Code’da `/game-localization` çağrısını kullanın. Elle kurulum için `game-localization/` klasörünün tamamını proje içindeki `.claude/skills/` ya da kullanıcı dizinindeki `~/.claude/skills/` yoluna kopyalayın. [Claude Code beceri kılavuzu](https://code.claude.com/docs/en/skills)

Barındırılan ChatGPT ve Claude sürümlerinde hesabın yükleme veya kurulum seçeneklerini kullanın. Sohbette bahsetmek kurulu beceriyi çağırır. Paylaşılabilir bağlantı için platformun desteklediği dizinde yayımlayın veya beceriyi ya da eklentiyi uygun bir çalışma alanında paylaşın. [ChatGPT eklentisi paylaşımı](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Claude becerisi paylaşımı](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Beceriyi kullanma

1. Kaynak metni veya dosyayı ve hedef diller için güncel proje terim sözlüğünü ekleyin. Sözlük yoksa taslağını hazırlamasını açıkça isteyin.
2. Kaynak ve hedef dilleri, platformu, içerik türünü ve çıktı biçimini belirtin. Gerektiğinde karakter sınırı, ekran görüntüsü, konuşmacı notu veya değişken örneği ekleyin.
3. Hesap tablolarında kaynak ve hedef sütunları belirtip yeni bir kopya isteyin. Oyun metinleri için sabit kimlik veya anahtar verin. Mağaza metni için hedef alanı ve varsa kesin uzunluk sınırını belirtin.
4. Çıktının kullanıma hazır mı yoksa hâlâ taslak mı olduğunu ayrı teslim notlarından öğrenin. Notlarda dosya kontrolü, dil incelemesi ve oyun içi ya da mağaza önizlemesindeki kontrol ayrı ayrı gösterilir. Her açık sorun için sonraki adım belirtilir. Terimleri tekrar kullanmadan önce proje sözlüğünde onaylayın.

Oyun arayüzü için teslim raporu ekranı, dize kimliğini, senaryoyu yeniden oluşturma adımlarını ve başarı ölçütünü içeren öncelikli bir kontrol listesi sunar. Önce uzun değişken değerleri ve kesilebilecek metinler kontrol edilir. Yazı tipi ve kullanılabilir genişlik biliniyorsa beceri gereken alanı tahmin edebilir. [Oyun içi kontroller](../game-localization/references/in-build-qa.md)

Onaylanan terimleri önerilerden ayrı tutmak için [proje sözlüğü şablonunu](../game-localization/references/project-glossary-template.md) kullanın. Güncellenen dosyayı kaydedip sonraki sohbete ekleyin.

**Hesap tablosu için örnek istem**

~~~text
Ekli çalışma kitabının ENGLISH sütununu Game Localization ile Almancaya (de-DE) çevir. Çevirileri yeni bir .xlsx kopyasında GERMAN sütununa yaz. Ekli terim sözlüğünü ve DESCRIPTION sütununu bağlam için kullan. Anahtarları, kaynak sütunları, yer tutucuları ve etiketleri koru. Terminoloji sorularını ve kontrol sonuçlarını satır kimlikleriyle ayrı listele.
~~~

Desteklenen `.xlsx` dosyaları için çalışma sayfasını, başlık satırını, sabit kimliklerin bulunduğu sütunu, kaynak sütunu ve mevcut hedef sütunu belirtin. Python 3.9 veya üzeriyle beceri, çevirileri kimliğe göre yeni bir kopyaya yazar ve çalışma kitabının geri kalanının korunduğunu kontrol eder. Çalışma kitabı doğrulanamazsa kimlikleri içeren bir CSV önerebilir. [Excel yönergeleri](../game-localization/references/xlsx-qa.md)

**Mağaza sayfası için örnek istem**

~~~text
Bu kısa Steam açıklamasını Game Localization ile İngilizceden Brezilya Portekizcesine (pt-BR) yerelleştir. Gerekirse taslak bir sözlük başlat. Oyun adını koru ve belirtilen karakter sınırına uy. Mağaza metnini ve teslim notlarını ayrı ver.
~~~

### CSV çevirilerini kontrol etme

Sabit satır kimlikleri olan bir CSV dosyası için kimlik, kaynak metin ve çeviri sütunlarının başlıklarını belirtin. Python 3.9 veya üstü kullanılabiliyorsa beceri kaynak dosyayı çevrilmiş dosyayla karşılaştırır. Eksik veya yinelenen kimlikleri, boş çevirileri, desteklenen yer tutucu veya etiketlerdeki değişiklikleri ve aşılan uzunluk sınırlarını bildirir. [CSV kontrolü yönergeleri](../game-localization/references/csv-qa.md)

Bir çeviriyi güncellemek için önceki ve güncel kaynak CSV dosyalarını, onaylı çevirileri ve sonraki editör düzeltmelerini ekleyin. Beceri, satırları kimliğe göre eşleştirir, değişmeyen satırlardaki kullanılabilir çevirileri korur ve eklenen, değiştirilen ya da silinen satırları işaretler. Uzun diyaloglarda aynı çalışma dosyasıyla devam etmek için her sahneden sonra ilerlemeyi kaydedin. [CSV çevirilerini güncelleme](../game-localization/references/csv-updates.md)

Çeviri taslağı, onaylı sözlük ve örnek teslim notları içeren [12 satırlık başlangıç örneğini](../game-localization/examples/first-run/README.md) deneyin.

### Kullandığımız model ayarları

| Ortam | Model | Akıl yürütme düzeyi |
| --- | --- | --- |
| ChatGPT Work veya Codex | GPT-6.1 Sol | Varsa High veya üzeri |
| Claude | Claude Opus 5.5 | Varsa High veya üzeri |

**High+**, uygulamada bulunan High ya da daha yüksek düzeyi ifade eder. Modeli ve düzeyi uygulamada seçin. Beceri bu tercihten bağımsız çalışır. [OpenAI model ayarları](https://learn.chatgpt.com/docs/models) · [Claude akıl yürütme düzeyleri](https://platform.claude.com/docs/en/build-with-claude/effort)

## Güncelleme veya kaldırma

| Kurulum türü | Güncelleme | Kaldırma |
| --- | --- | --- |
| ChatGPT veya Codex eklentisi | Yüklemeyi yönetiyorsanız eklenti ayrıntılarından **Upload new version** seçeneğini seçin. Dizin veya çalışma alanından kurulan eklentiler güncellemeyi aynı kaynaktan alır. | **Plugins → Installed → Game Localization** yolunu açıp varsa **Uninstall plugin** seçeneğini seçin. Yönetilen kurulum için yöneticiye danışın. |
| Bağımsız ChatGPT becerisi | Beceri yönetiminden kişisel yüklemenizi en yeni bağımsız ZIP ile değiştirin. | **Plugins → Skills** bölümünde **Installed** veya **Created by me** altında beceriyi bulup kaldırma seçeneğini kullanın. Çalışma alanına ait becerileri yöneticiler yönetir. |
| Özel Claude becerisi | Yönetim sayfasından yeni bağımsız ZIP’i yükleyin. İkinci bir kayıt oluşursa eskisini devre dışı bırakın. | Beceriyi **Customize → Skills** veya **Plugins** bölümünde açıp kapatın. Kendi yüklemeniz için **⋯ → Delete** seçeneğini seçip onaylayın. |
| Skills CLI ile kurulan yerel beceri | İzlenen bir dal için `npx skills update game-localization` komutunu çalıştırın veya yeni etiketten kurun. | Aynı projede `npx skills remove game-localization` komutunu çalıştırın. Genel kurulum yaptıysanız `-g` ekleyin. |
| Yerel klasör veya Codex Skill Installer | Kurulu `game-localization/` klasörünü en yeni sürümle değiştirin. | `game-localization/` klasörünü kaldırın. Codex, `.agents/skills/`, `~/.agents/skills/` veya `~/.codex/skills/` yolundan yükleyebilir. Claude Code, `.claude/skills/` veya `~/.claude/skills/` yolunu kullanır. Gerekirse yeni oturum açın. |

[OpenAI eklentilerini yönetme](https://learn.chatgpt.com/docs/plugins) · [Özel Claude becerilerini yönetme](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Kaynak kodu ve paketleme

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) becerinin ne zaman çalışacağını ve bir metin grubunu nasıl işleyeceğini tanımlar.
- [`game-localization/references/`](../game-localization/references/) kuralları ve başlangıç sözlüğünün dil sürümlerini içerir.
- [`packaging/chatgpt/`](../packaging/chatgpt/) eklenti bildirim dosyasını ve simgesini içerir.
- [`packages/`](../packages/) yüklemeye hazır arşivleri içerir.

İki ZIP’i aynı kaynaktan yeniden oluşturmak için deponun kökünde Python 3.9 veya üstüyle `python scripts/package.py` çalıştırın. Sürüm, ChatGPT eklentisinin bildirim dosyasından alınır. Dağıtımdan önce her ZIP’i ilgili ürüne yükleyin ve sözlükle korunan bir yer tutucu içeren küçük bir metin grubuyla deneyin.

## Lisans

Game Localization [MIT Lisansı](../LICENSE) kapsamında sunulur. Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Geliştiriciyi destekleyin

Game Localization ekibinize yardımcı oluyorsa [DonationAlerts üzerinden Maled1kt’i destekleyebilirsiniz](https://www.donationalerts.com/r/maled1kt). Bağış tamamen isteğe bağlıdır.
