/**
 * ThreadNote (Threads App Clone)
 * Features:
 * - 2단 카테고리 네비게이션 (대분류 + 소분류)
 * - TXT 파일 업로드로 스레드 추가 (영구 저장)
 * - 소분류 추가/삭제 관리
 * - Infinite Scroll Feed
 */

document.addEventListener("DOMContentLoaded", () => {
  // ── State ──
  let currentNavTab = "home";
  let activeMainCat = "all";       // 현재 선택된 대분류 ID
  let activeSubCat = "";           // 현재 선택된 소분류명 ("추천" or 소분류명)
  let currentPersona = "elementary_teacher";
  let feedThreads = [];
  let savedThreadIds = new Set();
  let likedThreadIds = new Set();
  let currentPage = 1;
  let isFetchingMore = false;
  let hasMoreThreads = true;
  let categoryData = null;          // /api/categories 응답 캐시
  let uploadThreadFile = null;      // 업로드 대기 중인 TXT 파일

  // Local Storage Keys
  const STORAGE_SAVED = "threads_saved_ids";
  const STORAGE_LIKES = "threads_liked_ids";
  const STORAGE_THEME = "threads_theme";
  const STORAGE_PERSONA = "threads_active_persona";

  const personasData = {
    elementary_teacher: { id: "elementary_teacher", name: "초등 3년차 김교사", handle: "elementary_kim", avatar: "👩‍🏫", badge: "교실 현실 썰", intro: "오늘도 2학년 교실에서 애들이랑 뒹굴다 멘탈 털린 초등교사의 생생한 수업 썰과 지도 꿀팁 🍎", followers: "14.2K" },
    pass_candidate: { id: "pass_candidate", name: "임용 수석합격생 박선배", handle: "pass_onepoint", avatar: "📚", badge: "출제 함정 팩폭", intro: "초등 임용고시 각론 단권화 마스터. 출제위원들이 눈에 불 켜고 파놓은 함정 포인트만 족집게처럼 풂 🧵", followers: "32.1K" },
    extreme_t_math: { id: "extreme_t_math", name: "극T 수학교육 분석관", handle: "math_extreme_t", avatar: "⚡", badge: "3줄 팩트폭격", intro: "감정 빼고 수학적 공준과 지도서 원리로만 말합니다. 반박 시 님 증명이 오개념임.", followers: "9.8K" },
    student_minsoo: { id: "student_minsoo", name: "2학년 3반 김민수", handle: "elem_minsoo", avatar: "🎒", badge: "초딩의 일기", intro: "오늘 선생님이 종이 두 번 접으라고 하더니 직각이래요... 왜 각도기 안 쓰고 손으로 접음? 억울함", followers: "6.4K" },
    cat_teacher: { id: "cat_teacher", name: "냥집사 수학쌤", handle: "cat_math_teacher", avatar: "🐱", badge: "냥생철학", intro: "우리 집 치즈냥이 택배 상자 굴리는 거 보다가 깨달은 직육면체와 밑면의 위대한 법칙 🐾", followers: "21.5K" },
    super_veteran: { id: "super_veteran", name: "교단 30년차 최부장", handle: "veteran_cho", avatar: "👴", badge: "부장님의 통찰", intro: "교단에서 분필 잡은 지 30년. 후배 교사들의 지도안을 1초 만에 꿰뚫어 보는 관록의 교육학 썰", followers: "18.3K" },
    pass_retry: { id: "pass_retry", name: "독서실 사활 건 N수생", handle: "pass_or_die", avatar: "🔥", badge: "피눈물 암기법", intro: "새벽 2시 독서실에서 지도서 백구 단권화 찢을 뻔한 수험생의 눈물겨운 암기 치트키 방출 ✍️", followers: "15.7K" },
    edutech_innovator: { id: "edutech_innovator", name: "에듀테크 AI 선도 정쌤", handle: "edutech_jung", avatar: "💻", badge: "디지털 각론", intro: "지오지브라, 알지오매스, 블록코딩으로 초등 수학·실과 각론을 3D로 해체하는 얼리어답터 교사", followers: "11.2K" },
    liberal_arts_mom: { id: "liberal_arts_mom", name: "초4맘 교육 인플루언서", handle: "mom_insight", avatar: "🌸", badge: "엄마의 시선", intro: "초4 아이 수학 숙제 봐주다 지도서 각론 읽고 경악한 문과 엄마의 사이다 교육 썰 ☕", followers: "26.4K" },
    science_lab_specialist: { id: "science_lab_specialist", name: "과학실험 전담 송교사", handle: "science_song", avatar: "🧪", badge: "실험실 비화", intro: "오늘도 비커 깨질 뻔한 위기를 넘긴 과학 전담 교사. 귀추적 추론과 순환학습 모형으로 과학 씹어먹기", followers: "13.9K" },
    english_native_buddy: { id: "english_native_buddy", name: "원어민 협력교사 크리스", handle: "teacher_chris", avatar: "🗽", badge: "원어민 팩폭", intro: "Korean 초등 영어 수업 참관하며 Noticing 오류 피드백과 파열음 최소대립쌍 코칭하는 미국인 쌤 🇺🇸", followers: "16.8K" },
    pe_sports_coach: { id: "pe_sports_coach", name: "체육부장 강코치", handle: "pe_coach_kang", avatar: "🏃‍♂️", badge: "체육관 호루라기", intro: "수영장 과호흡 응급처치부터 라반의 움직임 4요소까지, 몸으로 증명하는 초등 체육 각론 썰 ⚽", followers: "17.4K" },
    art_music_maestro: { id: "art_music_maestro", name: "예체능 감성 전담 한쌤", handle: "art_music_han", avatar: "🎨", badge: "예체능 아틀리에", intro: "판화 찍을 때 숟가락으로 문지르고, 6/8박자 노래에 장구 장단 얹는 융합 예술 수업의 달인 🎶", followers: "14.7K" },
    morality_philosopher: { id: "morality_philosopher", name: "도덕과 철학자 윤교사", handle: "moral_ethic_yoon", avatar: "⚖️", badge: "인성 나침반", intro: "교실 싸움 중재할 때 아리스토텔레스와 칸트를 소환하는 찐 윤리학 덕후 초등교사 🏛️", followers: "12.0K" },
    exam_evaluator: { id: "exam_evaluator", name: "전직 출제위원 장학사 Q", handle: "evaluator_q", avatar: "🧐", badge: "칼채점 주의보", intro: "임용 1차 채점관 경험 다수. 수험생들이 어디서 키워드 빼먹고 0.5점 깎여 탈락하는지 적나라하게 공개", followers: "45.2K" },
    practical_smartfarm: { id: "practical_smartfarm", name: "실과 스마트팜 지도교사", handle: "smartfarm_teacher", avatar: "🌱", badge: "스마트 텃밭", intro: "킬패트릭 프로젝트로 방울토마토 키우고 토양수분센서 엔트리로 제어하는 미래 농업 교육자 🍅", followers: "10.5K" }
  };

  function getPersonaMeta(pId) {
    return personasData[pId] || personasData.elementary_teacher;
  }

  // ── Elements ──
  const timelineView = document.getElementById("timelineView");
  const searchView = document.getElementById("searchView");
  const activityView = document.getElementById("activityView");
  const profileView = document.getElementById("profileView");
  const threadsFeedStream = document.getElementById("threadsFeedStream");
  const feedEmptyNotice = document.getElementById("feedEmptyNotice");
  const feedWelcomeTitle = document.getElementById("feedWelcomeTitle");
  const feedWelcomeDesc = document.getElementById("feedWelcomeDesc");
  const feedWelcomeEmoji = document.querySelector(".feed-welcome-emoji");

  // 2단 카테고리 바
  const mainCatBar = document.getElementById("mainCatBar");
  const subCatBar = document.getElementById("subCatBar");

  // Infinite Scroll Sentinel
  const infiniteScrollSentinel = document.getElementById("infiniteScrollSentinel");
  const infiniteSpinner = document.getElementById("infiniteSpinner");

  // Nav & Controls
  const bottomNavBtns = document.querySelectorAll(".bnav-btn");
  const themeToggleBtn = document.getElementById("themeToggleBtn");
  const homeLogoBtn = document.getElementById("homeLogoBtn");

  // Upload Thread Modal
  const openUploadThreadBtn = document.getElementById("openUploadThreadBtn");
  const uploadThreadModal = document.getElementById("uploadThreadModal");
  const closeUploadThreadModalBtn = document.getElementById("closeUploadThreadModalBtn");
  const uploadThreadDropArea = document.getElementById("uploadThreadDropArea");
  const uploadThreadFileInput = document.getElementById("uploadThreadFileInput");
  const uploadThreadFileName = document.getElementById("uploadThreadFileName");
  const uploadThreadSubmitBtn = document.getElementById("uploadThreadSubmitBtn");
  const uploadThreadProgress = document.getElementById("uploadThreadProgress");
  const uploadThreadProgressFill = document.getElementById("uploadThreadProgressFill");
  const uploadThreadProgressText = document.getElementById("uploadThreadProgressText");

  // Compose Modal
  const bottomComposeBtn = document.getElementById("bottomComposeBtn");
  const composeModal = document.getElementById("composeModal");
  const closeComposeModalBtn = document.getElementById("closeComposeModalBtn");
  const submitComposeBtn = document.getElementById("submitComposeBtn");
  const composeTextArea = document.getElementById("composeTextArea");
  const modalAuthorAvatar = document.getElementById("modalAuthorAvatar");
  const modalAuthorName = document.getElementById("modalAuthorName");
  const currentPersonaLabel = document.getElementById("currentPersonaLabel");
  const openPersonaPicker = document.getElementById("openPersonaPicker");
  const personaPickerDropdown = document.getElementById("personaPickerDropdown");
  const personaOptionItems = document.querySelectorAll(".persona-option-item");

  const modalAttachBtn = document.getElementById("modalAttachBtn");
  const modalFileInput = document.getElementById("modalFileInput");
  const quickMathSampleBtn = document.getElementById("quickMathSampleBtn");
  const composePdfBadge = document.getElementById("composePdfBadge");
  const pdfFileName = document.getElementById("pdfFileName");
  const pdfFileSize = document.getElementById("pdfFileSize");
  const removePdfBtn = document.getElementById("removePdfBtn");

  // Search & Activity
  const searchInput = document.getElementById("searchInput");
  const searchChips = document.querySelectorAll(".search-chip");
  const searchResultsStream = document.getElementById("searchResultsStream");
  const activityStream = document.getElementById("activityStream");
  const activityEmptyNotice = document.getElementById("activityEmptyNotice");
  const actTabs = document.querySelectorAll(".act-tab");

  // Profile & Settings
  const profileFeedStream = document.getElementById("profileFeedStream");
  const openSettingsBtn = document.getElementById("openSettingsBtn");
  const switchPersonaBtn = document.getElementById("switchPersonaBtn");
  const settingsModal = document.getElementById("settingsModal");
  const closeSettingsModalBtn = document.getElementById("closeSettingsModalBtn");

  // Toast
  const threadsToast = document.getElementById("threadsToast");
  const threadsToastText = document.getElementById("threadsToastText");

  // ==========================================
  // 1. Initialization
  // ==========================================
  init();

  async function init() {
    console.log("[ThreadNote] Starting initialization...");
    try { loadStoredPreferences(); } catch(e) { console.error("[Init] loadStoredPreferences failed:", e); }
    try { await setupCategoryNav(); } catch(e) { console.error("[Init] setupCategoryNav failed:", e); }
    try { setupNavigation(); } catch(e) { console.error("[Init] setupNavigation failed:", e); }
    try { setupUploadThread(); } catch(e) { console.error("[Init] setupUploadThread failed:", e); }
    try { setupSettingsModal(); } catch(e) { console.error("[Init] setupSettingsModal failed:", e); }
    try { setupFeedInteractions(); } catch(e) { console.error("[Init] setupFeedInteractions failed:", e); }
    try { setupComposeModal(); } catch(e) { console.error("[Init] setupComposeModal failed:", e); }
    try { setupSearch(); } catch(e) { console.error("[Init] setupSearch failed:", e); }
    try { setupActivityAndProfile(); } catch(e) { console.error("[Init] setupActivityAndProfile failed:", e); }
    try { await loadInitialFeed(); } catch(e) { console.error("[Init] loadInitialFeed failed:", e); }
    try { setupInfiniteScroll(); } catch(e) { console.error("[Init] setupInfiniteScroll failed:", e); }
    console.log("[ThreadNote] Initialization complete!");
  }

  function loadStoredPreferences() {
    const savedTheme = localStorage.getItem(STORAGE_THEME) || "dark";
    setTheme(savedTheme);
    try {
      const saved = localStorage.getItem(STORAGE_SAVED);
      if (saved) savedThreadIds = new Set(JSON.parse(saved));
      const likes = localStorage.getItem(STORAGE_LIKES);
      if (likes) likedThreadIds = new Set(JSON.parse(likes));
      const persona = localStorage.getItem(STORAGE_PERSONA);
      if (persona) currentPersona = persona;
    } catch (e) { console.warn(e); }
    updatePersonaUI();
  }

  function setTheme(theme) {
    document.body.classList.toggle("dark-theme", theme === "dark");
    document.body.classList.toggle("light-theme", theme === "light");
    localStorage.setItem(STORAGE_THEME, theme);
  }

  // ==========================================
  // 2. 2단 카테고리 네비게이션
  // ==========================================
  async function setupCategoryNav() {
    const res = await fetch("/api/categories");
    categoryData = await res.json();
    renderMainCatBar();
  }

  function renderMainCatBar() {
    if (!mainCatBar || !categoryData) return;
    mainCatBar.innerHTML = "";
    categoryData.main_categories.forEach(cat => {
      const btn = document.createElement("button");
      btn.className = "main-cat-btn" + (cat.id === activeMainCat ? " active" : "");
      btn.dataset.catId = cat.id;
      btn.textContent = `${cat.emoji} ${cat.label}`;
      btn.addEventListener("click", () => onMainCatClick(cat));
      mainCatBar.appendChild(btn);
    });
  }

  function onMainCatClick(cat) {
    activeMainCat = cat.id;
    activeSubCat = "";
    // Update active style
    mainCatBar.querySelectorAll(".main-cat-btn").forEach(b => b.classList.toggle("active", b.dataset.catId === cat.id));

    // Update welcome header
    if (feedWelcomeTitle) feedWelcomeTitle.textContent = cat.id === "all" ? "추천 피드" : `${cat.emoji} ${cat.label}`;
    if (feedWelcomeDesc) feedWelcomeDesc.textContent = cat.id === "all" ? "모든 과목에서 랜덤으로 선별된 핵심 지식 스레드" : `${cat.label} 과목의 전체 스레드`;
    if (feedWelcomeEmoji) feedWelcomeEmoji.textContent = cat.emoji || "🧵";

    // Show/hide sub-cat bar
    if (cat.id === "all") {
      subCatBar.style.display = "none";
    } else {
      renderSubCatBar(cat.id);
      subCatBar.style.display = "flex";
    }

    resetAndLoadFeed();
  }

  function renderSubCatBar(mainId) {
    if (!subCatBar || !categoryData) return;
    const subs = categoryData.sub_categories[mainId] || [];
    subCatBar.innerHTML = "";

    // Always show ⭐추천 chip first
    const recChip = document.createElement("button");
    recChip.className = "sub-cat-chip active";
    recChip.dataset.sub = "추천";
    recChip.textContent = "⭐ 추천";
    recChip.addEventListener("click", () => onSubCatClick("추천", mainId));
    subCatBar.appendChild(recChip);

    subs.forEach(sub => {
      const chip = document.createElement("button");
      chip.className = "sub-cat-chip";
      chip.dataset.sub = sub;
      chip.textContent = sub;
      chip.addEventListener("click", () => onSubCatClick(sub, mainId));
      subCatBar.appendChild(chip);
    });
  }

  function onSubCatClick(subName, mainId) {
    activeSubCat = subName;
    subCatBar.querySelectorAll(".sub-cat-chip").forEach(c => c.classList.toggle("active", c.dataset.sub === subName));
    const cat = categoryData.main_categories.find(c => c.id === mainId);
    if (feedWelcomeTitle) feedWelcomeTitle.textContent = subName === "추천" ? `${cat?.emoji || ""} ${cat?.label || ""} 추천` : subName;
    if (feedWelcomeDesc) feedWelcomeDesc.textContent = subName === "추천" ? `${cat?.label} 전체에서 랜덤 추천` : `${cat?.label} > ${subName} 스레드`;
    resetAndLoadFeed();
  }

  function resetAndLoadFeed() {
    currentPage = 1;
    hasMoreThreads = true;
    feedThreads = [];
    if (threadsFeedStream) threadsFeedStream.innerHTML = "";
    loadInitialFeed();
  }

  // ==========================================
  // 3. TXT 스레드 파일 업로드
  // ==========================================
  function setupUploadThread() {
    // 업로드 버튼 → 모달 열기
    openUploadThreadBtn?.addEventListener("click", () => {
      uploadThreadModal?.classList.remove("hidden");
    });
    closeUploadThreadModalBtn?.addEventListener("click", () => {
      uploadThreadModal?.classList.add("hidden");
      resetUploadModal();
    });

    // 내보내기 버튼 클릭
    const exportThreadsBtn = document.getElementById("exportThreadsBtn");
    exportThreadsBtn?.addEventListener("click", () => {
      showToast("📥 모든 스레드 다운로드를 시작합니다...");
      window.location.href = "/api/export-threads";
    });

    // 드롭 영역 클릭 → 파일 선택
    uploadThreadDropArea?.addEventListener("click", () => uploadThreadFileInput?.click());

    // 파일 선택
    uploadThreadFileInput?.addEventListener("change", e => {
      const file = e.target.files?.[0];
      if (file) setUploadFile(file);
    });

    // 드래그 앤 드롭
    uploadThreadDropArea?.addEventListener("dragover", e => { e.preventDefault(); uploadThreadDropArea.classList.add("drag-over"); });
    uploadThreadDropArea?.addEventListener("dragleave", () => uploadThreadDropArea.classList.remove("drag-over"));
    uploadThreadDropArea?.addEventListener("drop", e => {
      e.preventDefault();
      uploadThreadDropArea.classList.remove("drag-over");
      const file = e.dataTransfer.files?.[0];
      if (file) setUploadFile(file);
    });

    // 제출
    uploadThreadSubmitBtn?.addEventListener("click", submitUploadThread);
  }

  function setUploadFile(file) {
    uploadThreadFile = file;
    if (uploadThreadFileName) uploadThreadFileName.textContent = `📄 ${file.name} (${Math.round(file.size / 1024)}KB)`;
    if (uploadThreadSubmitBtn) uploadThreadSubmitBtn.disabled = false;
  }

  async function submitUploadThread() {
    if (!uploadThreadFile) return;
    uploadThreadSubmitBtn.disabled = true;
    uploadThreadProgress?.classList.remove("hidden");
    if (uploadThreadProgressFill) uploadThreadProgressFill.style.width = "30%";
    if (uploadThreadProgressText) uploadThreadProgressText.textContent = "파일 읽는 중...";

    try {
      const text = await uploadThreadFile.text();
      if (uploadThreadProgressFill) uploadThreadProgressFill.style.width = "60%";
      if (uploadThreadProgressText) uploadThreadProgressText.textContent = "서버에 전송 중...";

      const res = await fetch("/api/upload-thread", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, filename: uploadThreadFile.name })
      });
      const data = await res.json();

      if (uploadThreadProgressFill) uploadThreadProgressFill.style.width = "100%";
      if (data.success) {
        uploadThreadProgressText.textContent = `✅ ${data.count}개 스레드 추가 완료!`;
        showToast(`🎉 ${data.count}개 스레드가 피드에 추가되었습니다!`);
        setTimeout(() => {
          uploadThreadModal?.classList.add("hidden");
          resetUploadModal();
          resetAndLoadFeed();
        }, 1200);
      } else {
        uploadThreadProgressText.textContent = `❌ 오류: ${data.error}`;
        uploadThreadSubmitBtn.disabled = false;
      }
    } catch (e) {
      if (uploadThreadProgressText) uploadThreadProgressText.textContent = `❌ 네트워크 오류`;
      uploadThreadSubmitBtn.disabled = false;
    }
  }

  function resetUploadModal() {
    uploadThreadFile = null;
    if (uploadThreadFileName) uploadThreadFileName.textContent = "";
    if (uploadThreadSubmitBtn) uploadThreadSubmitBtn.disabled = true;
    if (uploadThreadProgress) uploadThreadProgress.classList.add("hidden");
    if (uploadThreadProgressFill) uploadThreadProgressFill.style.width = "0%";
    if (uploadThreadFileInput) uploadThreadFileInput.value = "";
  }

  // ==========================================
  // 4. 설정 모달 (소분류 관리)
  // ==========================================
  function setupSettingsModal() {
    openSettingsBtn?.addEventListener("click", () => {
      settingsModal?.classList.remove("hidden");
      populateSubMgrSelect();
    });
    closeSettingsModalBtn?.addEventListener("click", () => settingsModal?.classList.add("hidden"));

    const subMgrMainSelect = document.getElementById("subMgrMainSelect");
    const subMgrNewName = document.getElementById("subMgrNewName");
    const subMgrAddBtn = document.getElementById("subMgrAddBtn");

    subMgrMainSelect?.addEventListener("change", () => {
      renderSubMgrChips(subMgrMainSelect.value);
    });

    subMgrAddBtn?.addEventListener("click", async () => {
      const mainId = subMgrMainSelect?.value;
      const name = subMgrNewName?.value.trim();
      if (!mainId || !name) return showToast("⚠️ 대분류와 소분류 이름을 입력해주세요");
      const res = await fetch("/api/categories", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "add_sub", main_id: mainId, sub_name: name })
      });
      const data = await res.json();
      if (data.success) {
        if (categoryData) categoryData.sub_categories[mainId] = data.sub_categories;
        if (subMgrNewName) subMgrNewName.value = "";
        renderSubMgrChips(mainId);
        if (activeMainCat === mainId) renderSubCatBar(mainId);
        showToast(`✅ '${name}' 소분류가 추가되었습니다`);
      }
    });
  }

  function populateSubMgrSelect() {
    const sel = document.getElementById("subMgrMainSelect");
    if (!sel || !categoryData) return;
    sel.innerHTML = '<option value="">대분류 선택...</option>';
    categoryData.main_categories.filter(c => c.id !== "all").forEach(cat => {
      const opt = document.createElement("option");
      opt.value = cat.id;
      opt.textContent = `${cat.emoji} ${cat.label}`;
      sel.appendChild(opt);
    });
  }

  function renderSubMgrChips(mainId) {
    const wrap = document.getElementById("subMgrChipsWrap");
    if (!wrap || !categoryData) return;
    const subs = categoryData.sub_categories[mainId] || [];
    wrap.innerHTML = subs.length ? "" : '<span class="sub-mgr-hint">소분류가 없습니다. 추가해보세요!</span>';
    subs.forEach(sub => {
      const chip = document.createElement("span");
      chip.className = "sub-mgr-chip";
      chip.innerHTML = `${sub}<button class="sub-mgr-chip-del" data-sub="${sub}" data-main="${mainId}">×</button>`;
      chip.querySelector(".sub-mgr-chip-del").addEventListener("click", async (e) => {
        const s = e.target.dataset.sub, m = e.target.dataset.main;
        const res = await fetch("/api/categories", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ action: "remove_sub", main_id: m, sub_name: s })
        });
        const data = await res.json();
        if (data.success) {
          if (categoryData) categoryData.sub_categories[m] = data.sub_categories;
          renderSubMgrChips(m);
          if (activeMainCat === m) renderSubCatBar(m);
          showToast(`🗑️ '${s}' 소분류가 삭제되었습니다`);
        }
      });
      wrap.appendChild(chip);
    });
  }

  function fileToBase64(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => { resolve(reader.result.split(",")[1]); };
      reader.onerror = reject;
      reader.readAsDataURL(file);
    });
  }

  // ==========================================
  // 5. Infinite Scroll (무한 스크롤) Engine
  // ==========================================
  function setupInfiniteScroll() {
    const observer = new IntersectionObserver((entries) => {
      const first = entries[0];
      if (first.isIntersecting && !isFetchingMore && hasMoreThreads && currentNavTab === "home") {
        fetchNextBatch();
      }
    }, { rootMargin: "300px" });
    if (infiniteScrollSentinel) observer.observe(infiniteScrollSentinel);
  }

  async function fetchNextBatch() {
    isFetchingMore = true;
    currentPage += 1;
    if (infiniteSpinner) infiniteSpinner.style.display = "block";
    try {
      const url = buildFeedUrl(currentPage, 3);
      const res = await fetch(url);
      if (res.ok) {
        const data = await res.json();
        const newBatch = data.threads || [];
        if (newBatch.length > 0) {
          feedThreads.push(...newBatch);
          newBatch.forEach(thread => {
            const el = buildThreadElement(thread);
            threadsFeedStream.appendChild(el);
          });
        } else {
          hasMoreThreads = false;
        }
      }
    } catch (e) { console.warn("Infinite fetch error:", e); }
    finally { isFetchingMore = false; }
  }

  function buildFeedUrl(page, limit) {
    const params = new URLSearchParams({ page, limit, main_category: activeMainCat });
    if (activeSubCat) params.set("sub_category", activeSubCat);
    return `/api/feed?${params}`;
  }

  // ==========================================
  // 6. Initial Feed Load
  // ==========================================
  async function loadInitialFeed() {
    currentPage = 1;
    try {
      const res = await fetch(buildFeedUrl(1, 6));
      if (res.ok) {
        const data = await res.json();
        feedThreads = data.threads || [];
        renderFeed();
      }
    } catch (e) {
      console.warn("Could not load initial feed:", e);
    }
  }

  function renderFeed() {
    threadsFeedStream.innerHTML = "";

    if (feedThreads.length === 0) {
      feedEmptyNotice.classList.remove("hidden");
    } else {
      feedEmptyNotice.classList.add("hidden");
      feedThreads.forEach(thread => {
        const el = buildThreadElement(thread);
        threadsFeedStream.appendChild(el);
      });
    }
  }

  // ==========================================
  // 5. Threads Component Builder
  // ==========================================
  function buildThreadElement(thread) {
    const wrapper = document.createElement("article");
    wrapper.className = "thread-item-wrapper";
    wrapper.id = `thread_${thread.thread_id}`;

    const persona = thread.persona || {};
    const isSaved = savedThreadIds.has(thread.thread_id);
    const isLiked = likedThreadIds.has(thread.thread_id);
    const metrics = thread.metrics || { likes: 120, replies: 12, reposts: 34 };

    // 1. Author Header
    const headerHtml = `
      <div class="thread-row-header">
        <div class="author-profile-group">
          <div class="threads-avatar-ring" style="background: ${persona.bg_gradient || '#444'}">
            ${persona.avatar || '👩‍🏫'}
          </div>
          <div class="author-meta-text">
            <div class="author-line-1">
              <span class="author-display-name">${escapeHtml(persona.name || '선생님')}</span>
              <span class="author-badge-chip">${escapeHtml(persona.badge || '교육과정 썰')}</span>
            </div>
            <div class="author-line-2">
              <span class="author-username">@${escapeHtml(persona.handle || 'edu')}</span>
              <span class="thread-dot">•</span>
              <span class="thread-time">${escapeHtml(thread.created_at || '방금')}</span>
            </div>
          </div>
        </div>
        <div class="thread-top-right-tools">
          <button class="bookmark-action-btn ${isSaved ? 'saved' : ''}" data-action="bookmark" title="${isSaved ? '북마크 해제' : '북마크 저장'}">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="${isSaved ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
              <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
            </svg>
          </button>
        </div>
      </div>
    `;

    // 2. Thread Subposts Stream with Vertical Line Connector
    let streamHtml = '<div class="thread-flow-container">';
    (thread.posts || []).forEach((post, idx) => {
      const stepName = post.role === "hook" ? "1/3 시작 썰" : post.role === "story_twist" ? "2/3 각론 지식의 연결" : "3/3 오개념 & 꿀팁";
      streamHtml += `
        <div class="thread-subpost">
          <div class="thread-vertical-pipe"></div>
          <div class="thread-node-bullet"></div>
          <span class="thread-step-badge">${stepName}</span>
          <div class="thread-text-content">${formatRichText(post.text)}</div>
        </div>
      `;
    });

    // Tags
    if (thread.tags && thread.tags.length > 0) {
      streamHtml += '<div class="thread-tags-row">';
      thread.tags.forEach(tag => {
        streamHtml += `<span class="thread-tag-link">${escapeHtml(tag)}</span>`;
      });
      streamHtml += '</div>';
    }
    streamHtml += '</div>';

    // 3. Source Insight Accordion (지도서 원문 & 출제 포인트 엿보기)
    const insight = thread.source_insight || {};
    const insightHtml = `
      <div class="source-insight-accordion">
        <button class="insight-trigger-btn" data-action="toggle-insight">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="9" y1="18" x2="15" y2="18"></line>
            <line x1="10" y1="22" x2="14" y2="22"></line>
            <path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"></path>
          </svg>
          <span>💡 지도서 원문 & 출제 포인트 엿보기</span>
        </button>
        <div class="insight-panel-drawer hidden">
          <div class="insight-drawer-title-row">
            <span class="insight-code-badge">${escapeHtml(insight.curriculum_code || '2022 개정 각론')}</span>
          </div>
          <div class="insight-sec-title">${escapeHtml(insight.title || '단원 핵심')}</div>
          <div class="insight-original-quote">"${escapeHtml(insight.academic_quote || '')}"</div>
          <div class="insight-mechanism-box">
            <strong>🔍 썰로 풀어낸 핵심 메커니즘:</strong> ${formatRichText(insight.core_concept || '')}
          </div>
          ${insight.qna ? `<div class="insight-qna-box"><strong>📌 핵심 발문 / 유의사항:</strong> ${escapeHtml(insight.qna)}</div>` : ''}
        </div>
      </div>
    `;

    // 4. Action Row (Heart, Bubble, Repost, Paper Plane)
    const actionHtml = `
      <div class="threads-action-row">
        <!-- Like -->
        <button class="action-icon-btn ${isLiked ? 'liked' : ''}" data-action="like" title="좋아요">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="${isLiked ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
          <span class="like-num">${metrics.likes.toLocaleString()}</span>
        </button>

        <!-- Reply / Comment -->
        <button class="action-icon-btn" data-action="comment" title="답글">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
          </svg>
          <span class="reply-num">${(thread.simulated_comments?.length || metrics.replies).toLocaleString()}</span>
        </button>

        <!-- Repost -->
        <button class="action-icon-btn" data-action="repost" title="리포스트">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="17 1 21 5 17 9"></polyline>
            <path d="M3 11V9a4 4 0 0 1 4-4h14"></path>
            <polyline points="7 23 3 19 7 15"></polyline>
            <path d="M21 13v2a4 4 0 0 1-4 4H3"></path>
          </svg>
          <span class="repost-num">${metrics.reposts.toLocaleString()}</span>
        </button>

        <!-- Share / Copy -->
        <button class="action-icon-btn" data-action="share" title="스레드 텍스트 전체 복사">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="22" y1="2" x2="11" y2="13"></line>
            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
          </svg>
          <span>스레드 복사</span>
        </button>
      </div>

      <!-- Metrics Summary -->
      <div class="thread-metrics-summary">
        답글 ${(thread.simulated_comments?.length || metrics.replies).toLocaleString()}개 • 좋아요 ${metrics.likes.toLocaleString()}개
      </div>
    `;

    // 5. Replies Tray
    let commentsListHtml = '<div class="replies-tray-list">';
    (thread.simulated_comments || []).forEach(comm => {
      const author = comm.author || comm.persona_name || "수험생 멘토";
      const handle = comm.handle || (comm.persona_name ? comm.persona_name.replace(/[^a-zA-Z0-9가-힣_]/g, '') : "mentor");
      const content = comm.content || comm.text || "";
      const avatar = comm.avatar || '💬';
      commentsListHtml += `
        <div class="reply-cell">
          <div class="reply-cell-avatar">${avatar}</div>
          <div class="reply-cell-bubble">
            <div class="reply-cell-author">${escapeHtml(author)} <span style="font-weight:400; font-size:11px; color:var(--text-muted)">@${escapeHtml(handle)}</span></div>
            <div class="reply-cell-content">${formatRichText(content)}</div>
          </div>
        </div>
      `;
    });
    commentsListHtml += '</div>';

    const repliesHtml = `
      <div class="thread-replies-tray hidden">
        <div class="replies-tray-title">실시간 스레드 댓글 반응</div>
        ${commentsListHtml}
        <div class="reply-input-dock">
          <input type="text" class="reply-input-field" placeholder="이 썰에 공감 답글 남기기..." />
          <button class="reply-submit-btn" data-action="post-reply">게시</button>
        </div>
      </div>
    `;

    wrapper.innerHTML = headerHtml + streamHtml + insightHtml + actionHtml + repliesHtml;
    bindCardEvents(wrapper, thread);
    return wrapper;
  }

  function bindCardEvents(card, thread) {
    // 1. Bookmark
    const bookmarkBtn = card.querySelector('[data-action="bookmark"]');
    bookmarkBtn?.addEventListener("click", () => {
      const isSaved = savedThreadIds.has(thread.thread_id);
      if (isSaved) {
        savedThreadIds.delete(thread.thread_id);
        bookmarkBtn.classList.remove("saved");
        bookmarkBtn.querySelector("svg").setAttribute("fill", "none");
        showToast("북마크가 해제되었습니다.");
      } else {
        savedThreadIds.add(thread.thread_id);
        bookmarkBtn.classList.add("saved");
        bookmarkBtn.querySelector("svg").setAttribute("fill", "currentColor");
        showToast("스레드가 저장되었습니다! 📌");
      }
      localStorage.setItem(STORAGE_SAVED, JSON.stringify(Array.from(savedThreadIds)));
      if (currentNavTab === "activity") renderActivity();
    });

    // 2. Insight Accordion Toggle
    const insightBtn = card.querySelector('[data-action="toggle-insight"]');
    const drawer = card.querySelector('.insight-panel-drawer');
    insightBtn?.addEventListener("click", () => {
      drawer.classList.toggle("hidden");
      const isHidden = drawer.classList.contains("hidden");
      insightBtn.querySelector("span").textContent = isHidden ? "💡 지도서 원문 & 출제 포인트 엿보기" : "▲ 지도서 원문 접기";
    });

    // 3. Like
    const likeBtn = card.querySelector('[data-action="like"]');
    const likeNum = card.querySelector('.like-num');
    likeBtn?.addEventListener("click", () => {
      const isLiked = likedThreadIds.has(thread.thread_id);
      if (isLiked) {
        likedThreadIds.delete(thread.thread_id);
        likeBtn.classList.remove("liked");
        likeBtn.querySelector("svg").setAttribute("fill", "none");
        thread.metrics.likes--;
      } else {
        likedThreadIds.add(thread.thread_id);
        likeBtn.classList.add("liked");
        likeBtn.querySelector("svg").setAttribute("fill", "currentColor");
        thread.metrics.likes++;
      }
      likeNum.textContent = thread.metrics.likes.toLocaleString();
      localStorage.setItem(STORAGE_LIKES, JSON.stringify(Array.from(likedThreadIds)));
    });

    // 4. Repost
    const repostBtn = card.querySelector('[data-action="repost"]');
    const repostNum = card.querySelector('.repost-num');
    repostBtn?.addEventListener("click", () => {
      repostBtn.classList.toggle("reposted");
      const isRepost = repostBtn.classList.contains("reposted");
      thread.metrics.reposts += isRepost ? 1 : -1;
      repostNum.textContent = thread.metrics.reposts.toLocaleString();
      showToast(isRepost ? "내 스레드 피드로 리포스트되었습니다! 🔁" : "리포스트가 취소되었습니다.");
    });

    // 5. Toggle Comments Tray
    const commentBtn = card.querySelector('[data-action="comment"]');
    const tray = card.querySelector('.thread-replies-tray');
    commentBtn?.addEventListener("click", () => {
      tray.classList.toggle("hidden");
    });

    // 6. Post User Reply
    const replyInput = card.querySelector('.reply-input-field');
    const replyBtn = card.querySelector('[data-action="post-reply"]');
    const replyList = card.querySelector('.replies-tray-list');

    const handleSendReply = () => {
      const text = replyInput.value.trim();
      if (!text) return;
      const newComment = {
        author: "나 (스레더)",
        handle: "me",
        avatar: "😎",
        content: text
      };
      if (!thread.simulated_comments) thread.simulated_comments = [];
      thread.simulated_comments.push(newComment);

      const cell = document.createElement("div");
      cell.className = "reply-cell";
      cell.innerHTML = `
        <div class="reply-cell-avatar">${newComment.avatar}</div>
        <div class="reply-cell-bubble">
          <div class="reply-cell-author">${escapeHtml(newComment.author)} <span style="font-weight:400; font-size:11px; color:var(--text-muted)">@${escapeHtml(newComment.handle)}</span></div>
          <div class="reply-cell-content">${escapeHtml(newComment.content)}</div>
        </div>
      `;
      replyList.appendChild(cell);
      replyInput.value = "";
      card.querySelector('.reply-num').textContent = thread.simulated_comments.length;
      showToast("답글이 게시되었습니다!");
    };

    replyBtn?.addEventListener("click", handleSendReply);
    replyInput?.addEventListener("keydown", (e) => {
      if (e.key === "Enter") handleSendReply();
    });

    // 7. Share / Copy full thread to clipboard
    const shareBtn = card.querySelector('[data-action="share"]');
    shareBtn?.addEventListener("click", () => {
      copyThreadForPosting(thread);
    });
  }

  function copyThreadForPosting(thread) {
    let copyText = `🧵 [Threads] ${thread.persona?.name || '지식 스레드'}\n\n`;
    (thread.posts || []).forEach((post, i) => {
      copyText += `(${i + 1}/${thread.posts.length})\n${post.text}\n\n`;
    });
    if (thread.tags) {
      copyText += thread.tags.join(" ") + "\n\n";
    }
    copyText += `💡 지도서 출제 포인트: ${thread.source_insight?.title || ''}`;

    navigator.clipboard.writeText(copyText).then(() => {
      showToast("스레드 타래 전체가 클립보드에 복사되었습니다! 📋");
    }).catch(() => {
      showToast("복사에 실패했습니다.");
    });
  }

  // ==========================================
  // 6. Navigation & Bottom 5 Tabs
  // ==========================================
  function setupNavigation() {
    bottomNavBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        const target = btn.dataset.bnav;
        if (target === "compose") {
          openComposeModal();
        } else {
          switchNavTab(target);
        }
      });
    });

    homeLogoBtn?.addEventListener("click", () => {
      switchNavTab("home");
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    themeToggleBtn?.addEventListener("click", () => {
      const isDark = document.body.classList.contains("dark-theme");
      setTheme(isDark ? "light" : "dark");
    });
  }

  function switchNavTab(tab) {
    currentNavTab = tab;
    bottomNavBtns.forEach(b => {
      b.classList.toggle("active", b.dataset.bnav === tab);
    });

    timelineView.classList.toggle("hidden", tab !== "home");
    searchView.classList.toggle("hidden", tab !== "search");
    activityView.classList.toggle("hidden", tab !== "activity");
    profileView.classList.toggle("hidden", tab !== "profile");

    if (tab === "home") renderFeed();
    if (tab === "activity") renderActivity();
    if (tab === "profile") renderProfile();
  }

  // Feed Category Pills
  function setupFeedInteractions() {
    feedNavPills.forEach(pill => {
      pill.addEventListener("click", () => {
        feedNavPills.forEach(p => p.classList.remove("active"));
        pill.classList.add("active");
        activeCategory = pill.dataset.category;
        currentPage = 1;
        loadInitialFeed();
      });
    });
  }

  // ==========================================
  // 7. Compose Modal
  // ==========================================
  function setupComposeModal() {
    bottomComposeBtn?.addEventListener("click", openComposeModal);
    closeComposeModalBtn?.addEventListener("click", closeComposeModal);

    composeModal?.addEventListener("click", (e) => {
      if (e.target === composeModal) closeComposeModal();
    });

    composeTextArea?.addEventListener("input", () => {
      updatePostBtnState();
    });

    openPersonaPicker?.addEventListener("click", (e) => {
      e.stopPropagation();
      personaPickerDropdown?.classList.toggle("hidden");
    });

    document.addEventListener("click", (e) => {
      if (personaPickerDropdown && !personaPickerDropdown.contains(e.target) && e.target !== openPersonaPicker) {
        personaPickerDropdown.classList.add("hidden");
      }
    });

    modalAttachBtn?.addEventListener("click", () => {
      modalFileInput?.click();
    });

    quickMathSampleBtn?.addEventListener("click", async () => {
      showToast("초등수학 교육과정 지도서 샘플을 불러왔습니다!");
      composePdfBadge?.classList.remove("hidden");
      if (pdfFileName) pdfFileName.textContent = "수학 3-4 교육과정 나올각_unlocked.pdf";
      if (pdfFileSize) pdfFileSize.textContent = "67페이지 • 도형 / 측정 / 수와 연산";
      if (composeTextArea) composeTextArea.value = "초등수학 교육과정 지도서 각론 전 단원을 바탕으로 스레드 타래를 자동 구성합니다.";
      updatePostBtnState();
    });

    removePdfBtn?.addEventListener("click", () => {
      composePdfBadge?.classList.add("hidden");
      if (modalFileInput) modalFileInput.value = "";
      updatePostBtnState();
    });

    submitComposeBtn?.addEventListener("click", handlePublishThread);

    renderPersonaPickerOptions();
  }

  function renderPersonaPickerOptions() {
    if (!personaPickerDropdown) return;
    personaPickerDropdown.innerHTML = '<div class="popover-title">스레드 화자 선택 (16 페르소나)</div>';
    Object.keys(personasData).forEach(pId => {
      const p = personasData[pId];
      const isSel = pId === currentPersona;
      const item = document.createElement("div");
      item.className = `persona-option-item ${isSel ? "selected" : ""}`;
      item.dataset.persona = pId;
      item.innerHTML = `
        <span class="popover-avatar">${p.avatar}</span>
        <div class="popover-info">
          <strong>${p.name}</strong>
          <small>${p.badge ? p.badge + ' • ' : ''}${p.role || (p.intro ? p.intro.slice(0, 30) : '')}</small>
        </div>
        <span class="chk">${isSel ? "✓" : ""}</span>
      `;
      item.addEventListener("click", () => {
        currentPersona = pId;
        localStorage.setItem(STORAGE_PERSONA, currentPersona);
        updatePersonaUI();
        renderPersonaPickerOptions();
        personaPickerDropdown.classList.add("hidden");
        showToast(`화자가 [${p.name}] (으)로 변경되었습니다! ✨`);
        if (currentNavTab === "profile") {
          renderProfile();
        }
      });
      personaPickerDropdown.appendChild(item);
    });
  }

  function openComposeModal() {
    composeModal?.classList.remove("hidden");
    composeTextArea?.focus();
    renderPersonaPickerOptions();
    updatePersonaUI();
    updatePostBtnState();
  }

  function closeComposeModal() {
    composeModal?.classList.add("hidden");
  }

  function updatePersonaUI() {
    const pMeta = getPersonaMeta(currentPersona);
    if (modalAuthorAvatar) modalAuthorAvatar.textContent = pMeta.avatar;
    if (modalAuthorName) modalAuthorName.textContent = pMeta.name;
    if (currentPersonaLabel) currentPersonaLabel.textContent = `${pMeta.avatar} ${pMeta.name}`;

    const pName = document.getElementById("profileDisplayName");
    const pHandle = document.getElementById("profileHandle");
    const pAvatar = document.getElementById("profileLargeAvatar");
    const pBio = document.getElementById("profileBio");
    const pFollowers = document.getElementById("profileFollowers");
    if (pName) pName.textContent = pMeta.name;
    if (pHandle) pHandle.textContent = `@${pMeta.handle}`;
    if (pAvatar) pAvatar.textContent = pMeta.avatar;
    if (pBio) pBio.textContent = pMeta.intro;
    if (pFollowers) pFollowers.textContent = pMeta.followers || '14.2K';
  }

  function updatePostBtnState() {
    const hasText = composeTextArea && composeTextArea.value.trim().length > 0;
    const hasPdf = composePdfBadge && !composePdfBadge.classList.contains("hidden");
    if (submitComposeBtn) submitComposeBtn.disabled = !(hasText || hasPdf);
  }

  // Publish New Thread
  async function handlePublishThread() {
    submitComposeBtn.disabled = true;
    submitComposeBtn.textContent = "게시 중...";

    const userText = composeTextArea.value.trim();

    try {
      const res = await fetch("/api/convert-text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: userText || "초등수학 각론 지도 포인트",
          persona: currentPersona,
          title: pdfFileName?.textContent || "수학 지식 썰"
        })
      });

      if (res.ok) {
        const data = await res.json();
        if (data.thread) {
          feedThreads.unshift(data.thread);
          closeComposeModal();
          composeTextArea.value = "";
          composePdfBadge.classList.add("hidden");
          switchNavTab("home");
          renderFeed();
          showToast("스레드가 성공적으로 게시되었습니다! 🎉");
          window.scrollTo({ top: 0, behavior: "smooth" });
        }
      } else {
        throw new Error("서버 변환 오류");
      }
    } catch (err) {
      console.error(err);
      alert("스레드 게시 중 오류가 발생했습니다: " + err.message);
    } finally {
      submitComposeBtn.disabled = false;
      submitComposeBtn.textContent = "게시";
    }
  }

  // ==========================================
  // 8. Search Feature
  // ==========================================
  function setupSearch() {
    searchInput?.addEventListener("input", () => {
      executeSearch(searchInput.value.trim());
    });

    searchChips.forEach(chip => {
      chip.addEventListener("click", () => {
        searchInput.value = chip.dataset.query;
        executeSearch(chip.dataset.query);
      });
    });
  }

  function executeSearch(query) {
    searchResultsStream.innerHTML = "";
    if (!query) return;

    const matched = feedThreads.filter(t => {
      const title = t.source_insight?.title || "";
      const postsText = t.posts?.map(p => p.text).join(" ") || "";
      const tagsText = t.tags?.join(" ") || "";
      return title.includes(query) || postsText.includes(query) || tagsText.includes(query);
    });

    if (matched.length === 0) {
      searchResultsStream.innerHTML = `
        <div class="empty-notice">
          <div class="empty-threads-logo">🔍</div>
          <h3>'${escapeHtml(query)}' 검색 결과가 없습니다</h3>
          <p>다른 키워드나 단원명을 검색해보세요.</p>
        </div>
      `;
    } else {
      matched.forEach(thread => {
        const el = buildThreadElement(thread);
        searchResultsStream.appendChild(el);
      });
    }
  }

  // ==========================================
  // 9. Activity & Profile Tabs
  // ==========================================
  function setupActivityAndProfile() {
    actTabs.forEach(tab => {
      tab.addEventListener("click", () => {
        actTabs.forEach(t => t.classList.remove("active"));
        tab.classList.add("active");
        renderActivity(tab.dataset.actTab);
      });
    });

    openSettingsBtn?.addEventListener("click", () => {
      settingsModal.classList.remove("hidden");
    });

    closeSettingsModalBtn?.addEventListener("click", () => {
      settingsModal.classList.add("hidden");
    });

    settingsModal?.addEventListener("click", (e) => {
      if (e.target === settingsModal) settingsModal.classList.add("hidden");
    });

    geminiApiKeySetting?.addEventListener("change", () => {
      const key = geminiApiKeySetting.value.trim();
      if (key) {
        localStorage.setItem(STORAGE_APIKEY, key);
        showToast("Gemini API Key가 저장되었습니다.");
      } else {
        localStorage.removeItem(STORAGE_APIKEY);
        showToast("API Key가 삭제되었습니다.");
      }
    });

    switchPersonaBtn?.addEventListener("click", () => {
      openComposeModal();
      personaPickerDropdown.classList.remove("hidden");
    });
  }

  function renderActivity(type = "saved") {
    activityStream.innerHTML = "";
    const list = type === "saved"
      ? feedThreads.filter(t => savedThreadIds.has(t.thread_id))
      : feedThreads.filter(t => likedThreadIds.has(t.thread_id));

    if (list.length === 0) {
      activityEmptyNotice.classList.remove("hidden");
    } else {
      activityEmptyNotice.classList.add("hidden");
      list.forEach(thread => {
        const el = buildThreadElement(thread);
        activityStream.appendChild(el);
      });
    }
  }

  function renderProfile() {
    profileFeedStream.innerHTML = "";
    const myThreads = feedThreads.filter(t => t.persona?.id === currentPersona);

    if (myThreads.length === 0) {
      profileFeedStream.innerHTML = `
        <div class="empty-notice">
          <div class="empty-threads-logo">🧵</div>
          <h3>작성한 스레드가 없습니다</h3>
          <p>새 스레드를 작성하여 지식 썰을 공유해보세요.</p>
        </div>
      `;
    } else {
      myThreads.forEach(thread => {
        const el = buildThreadElement(thread);
        profileFeedStream.appendChild(el);
      });
    }
  }

  // Toast Helper
  function showToast(msg) {
    threadsToastText.textContent = msg;
    threadsToast.classList.remove("hidden");
    setTimeout(() => {
      threadsToast.classList.add("hidden");
    }, 2400);
  }

  function escapeHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function formatRichText(str) {
    if (!str) return "";
    let safe = escapeHtml(str);

    // 1. Math / LaTeX sanitization to clean readable unicode math
    safe = safe.replace(/\\textbf\{([^}]+)\}/g, '<strong class="highlight-bold">$1</strong>');
    safe = safe.replace(/\\text\{([^}]+)\}/g, '$1');
    safe = safe.replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, '$1/$2');
    safe = safe.replace(/\\times/g, '×');
    safe = safe.replace(/\\div/g, '÷');
    safe = safe.replace(/\\pm/g, '±');
    safe = safe.replace(/\\neq/g, '≠');
    safe = safe.replace(/\\leq?/g, '≤');
    safe = safe.replace(/\\geq?/g, '≥');
    safe = safe.replace(/\\approx/g, '≈');
    safe = safe.replace(/\\cdot/g, '·');
    safe = safe.replace(/\\dots/g, '…');
    safe = safe.replace(/\\square/g, '□');
    safe = safe.replace(/\\triangle/g, '△');
    safe = safe.replace(/\\pi/g, 'π');
    safe = safe.replace(/\\\((.*?)\\\)/g, '$1');
    safe = safe.replace(/\$(.*?)\$/g, '$1');

    // 2. Parse markdown bold: **word** -> <strong class="highlight-bold">$1</strong>
    safe = safe.replace(/\*\*(.*?)\*\*/g, '<strong class="highlight-bold">$1</strong>');
    return safe;
  }
});
