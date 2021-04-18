def SET_BG(BGID):
    set_BG(BGID)
    if(BGID == sty_bg_0031_100):
        bg_pos_x(60)
    elif(BGID == sty_bg_0004_100):
        bg_pos_x(45)
    elif(BGID == sty_bg_0033_101):
        bg_pos_x(10)
    elif(BGID == sty_bg_0002_100):
        bg_pos_x(75)
    elif(BGID == sty_bg_0003_100):
        bg_pos_x(40)
    elif(BGID == sty_bg_0016_103):
        bg_pos_x(68)
    elif(BGID == sty_bg_0049_100):
        bg_pos_x(-68)
    elif(BGID == sty_bg_0049_101):
        bg_pos_x(-68)

def push(A, CID):
    if(A == 0):
        c_push_t(CID)
    elif(A == 1):
        c_push_t_slow(CID)
    elif(A == 2):
        c_push_b(CID)
    else:
        pass

def eye1(CID, eye):
    if(eye == O):
        chara_eyeblink(CID, -1)
    elif(eye == Q):
        chara_eyeblink(CID, -2)
    elif(eye == M):
        chara_eyeblink(CID)
    else:
        chara_eyeblink(CID)

def lip1(CID, lip):
    if(lip == O):
        chara_lipsynch(CID, -2)
    elif(lip == Q):
        chara_lipsynch(CID, -1)
    elif(lip == M):
        chara_lipsynch(CID)
    else:
        chara_lipsynch(CID)

def effset(effectIds, triggers):
    set_BG_effect(effectIds)
    set_BG_effect_trigger(triggers)

def bgm(cmd, BGM):
    if(cmd == out):
        stop_bgm(0.5)
    elif(cmd == v_down):
        set_volume(0.5, 0.5, BGM)
    elif(cmd == mute):
        set_volume(0, 0.5, BGM)
    elif(cmd == v_def):
        set_volume(1.0, 0.5, BGM)

def window(cmd):
    if(cmd == f_in):
        window_fadein(0.5)
    elif(cmd == f_out):
        window_fadeout(0.5)
    elif(cmd == f_in_s):
        window_fadein(0.2)
    elif(cmd == f_out_s):
        window_fadeout(0.2)
    elif(cmd == bk_in):
        screen_fadein(1.0, 0, 0, 0)
    elif(cmd == bk_in_vs):
        screen_fadein(0.2, 0, 0, 0)
    elif(cmd == bk_in_md):
        screen_fadein(0.3, 0, 0, 0)
    elif(cmd == bk_in_s):
        screen_fadein(0.4, 0, 0, 0)
    elif(cmd == bk_in_l):
        screen_fadein(2.0, 0, 0, 0)
    elif(cmd == bk_in_vl):
        screen_fadein(4.0, 0, 0, 0)
    elif(cmd == farst_int):
        RESET_TEXT()
        window_fadeout(0, true)
        BGMFOUT_DEF()
        SEFOUT_DEF()
        screen_fadeout(1.0, 0, 0, 0)
    elif(cmd == bk_out):
        WFOUT_SHORT()
        screen_fadeout(1.0, 0, 0, 0)
    elif(cmd == bk_out_vs):
        WFOUT_SHORT()
        screen_fadeout(0.3, 0, 0, 0)
    elif(cmd == bk_out_ms):
        WFOUT_SHORT()
        screen_fadeout(0.6, 0, 0, 0)
    elif(cmd == bk_out_l):
        WFOUT_SHORT()
        screen_fadeout(2.0, 0, 0, 0)
    elif(cmd == bk_out_vl):
        WFOUT_SHORT()
        screen_fadeout(4.0, 0, 0, 0)
    elif(cmd == wt_in_ms):
        screen_fadein(0.6, 255, 255, 255)
    elif(cmd == wt_in):
        screen_fadein(1.0, 255, 255, 255)
    elif(cmd == wt_in_l):
        screen_fadein(2.0, 255, 255, 255)
    elif(cmd == wt_in_vl):
        screen_fadein(4.0, 255, 255, 255)
    elif(cmd == wt_out_pr_l):
        screen_fadeout(2.1, 255, 255, 255)
    elif(cmd == wt_out_pr_vs):
        screen_fadeout(0, 255, 255, 255)
    elif(cmd == wt_out_ms):
        WFOUT_SHORT()
        screen_fadeout(0.6, 255, 255, 255)
    elif(cmd == wt_out):
        WFOUT_SHORT()
        screen_fadeout(1.0, 255, 255, 255)
    elif(cmd == wt_out_l):
        WFOUT_SHORT()
        screen_fadeout(2.0, 255, 255, 255)
    elif(cmd == wt_out_vl):
        WFOUT_SHORT()
        screen_fadeout(4.0, 255, 255, 255)
    elif(cmd == trns_in_r):
        fade_color(0.25, 0, 0, 0, 0)
        screen_transin(1, 1.0)
    elif(cmd == trns_in_l):
        fade_color(0.25, 0, 0, 0, 0)
        screen_transin(2, 1.0)
    elif(cmd == trns_out_r):
        WFOUT_SHORT()
        screen_transout(2, 1.0)
        fade_color(0.25, 0, 0, 0, 1)
    elif(cmd == curtain):
        set_BG_effect(EFF_107)
        set_BG_effect_trigger(9)
    elif(cmd == curtaout):
        set_BG_effect(EFF_107)
        set_BG_effect_trigger(8)
        wait(0.5)
    else:
        pass

def c_set_def(eye, lip, POS, CID, int):
    CHARA_SET_0(eye, lip, POS, CID, int)

def c_set_W(act, cmd, eye, lip, POS, CID, int, int2):
    if(act == 'in'):
        if(cmd == 'def'):
            c_set_def(eye, lip, POS, CID, int)
            chara_face(CID, int2, 1)
            CHARA_FADEIN_DEF(CID)

def c_set(act, cmd, eye, lip, POS, CID, int):
    if(act == 'in'):
        if(cmd == 'def'):
            c_set_def(eye, lip, POS, CID, int)
            CHARA_FADEIN_DEF(CID)
        elif(cmd == 'kami'):
            c_set_def(eye, lip, POS, CID, int)
            KAMITE_IN_DEF(CID)

def c_jump2_em_high(CID):
    mnu_move(CID, true, 0.2, 0, 200, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -210, EaseInCubic)
    mnu_move(CID, false, 0.2, 0, 150, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -150, EaseInCubic)
    mnu_move(CID, false, 0.1, 0, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, 0, -4, EaseInCubic)
    cmp_move(CID, 1.0, 0, 0)

def BGMFOUT_DEF():
    stop_bgm(0.5)

def BGMTUNE_DOWN(BGM):
    set_volume(0.5, 0.5, BGM)

def BGMTUNE_DOWN_0(BGM):
    set_volume(0, 0.5, BGM)

def BGMTUNE_DEF(BGM):
    set_volume(1.0, 0.5, BGM)

def SEFOUT_DEF():
    stop_se(0.5)

def WFIN_DEF():
    window_fadein(0.5)

def WFOUT_DEF():
    window_fadeout(0.5)

def WFOUT_SHORT():
    window_fadeout(0.2)

def WFIN_SHORT():
    window_fadein(0.2)

def BLACK_IN_DEF():
    screen_fadein(1.0, 0, 0, 0)

def BLACK_IN_VERYSHORT():
    screen_fadein(0.2, 0, 0, 0)

def BLACK_IN_MIDSHORT():
    screen_fadein(0.3, 0, 0, 0)

def BLACK_IN_SHORT():
    screen_fadein(0.4, 0, 0, 0)

def BLACK_IN_LONG():
    screen_fadein(2.0, 0, 0, 0)

def BLACK_IN_VERYLONG():
    screen_fadein(4.0, 0, 0, 0)

def BLACK_OUT_DEF_STOP():
    RESET_TEXT()
    window_fadeout(0, true)
    BGMFOUT_DEF()
    SEFOUT_DEF()
    screen_fadeout(1.0, 0, 0, 0)

def BLACK_OUT_DEF_STOP_FIN(mode):
    RESET_TEXT()
    if(mode == 1):
        NO_EFFECT()
        touch_enable(false)
        window_fadeout(0, true)
        wait(0.5)
        fade_color(1.0, 0, 0, 0, 0.7, EaseLinear, true)
        wait(1.0)
        play_sound(SE_112)
        fin(true, 0, 170)
        set_BG_effect(EFF_125)
        touch_wait(0.5, 3.0)
        BGMFOUT_DEF()
        SEFOUT_DEF()
        fade_color(1.0, 0, 0, 0, 1)
    elif(mode == 2):
        NO_EFFECT()
        touch_enable(false)
        wait(1.5)
        play_sound(SE_112)
        fin(true, 0, 170)
        set_BG_effect(EFF_125)
        touch_wait(0.5, 3.0)
        BGMFOUT_DEF()
        SEFOUT_DEF()
        fade_color(1.0, 0, 0, 0, 1)
    elif(mode == 3):
        NO_EFFECT()
        touch_enable(false)
        window_fadeout(0, true)
        wait(1.5)
        play_sound(SE_112)
        fin(true, 0, 170)
        set_BG_effect(EFF_125)
        touch_wait(0.5, 3.0)
        BGMFOUT_DEF()
        SEFOUT_DEF()
        fade_color(1.0, 0, 0, 0, 1)

def BLACK_OUT_DEF():
    WFOUT_SHORT()
    screen_fadeout(1.0, 0, 0, 0)

def BLACK_OUT_VERYSHORT():
    WFOUT_SHORT()
    screen_fadeout(0.3, 0, 0, 0)

def BLACK_OUT_MIDSHORT():
    WFOUT_SHORT()
    screen_fadeout(0.6, 0, 0, 0)

def BLACK_OUT_LONG():
    WFOUT_SHORT()
    screen_fadeout(2.0, 0, 0, 0)

def WHITE_IN_MIDSHORT():
    screen_fadein(0.6, 255, 255, 255)

def WHITE_IN_DEF():
    screen_fadein(1.0, 255, 255, 255)

def WHITE_IN_LONG():
    screen_fadein(2.0, 255, 255, 255)

def WHITE_IN_VERYLONG():
    screen_fadein(4.0, 255, 255, 255)

def WHITE_OUT_MIDSHORT():
    WFOUT_SHORT()
    screen_fadeout(0.6, 255, 255, 255)

def WHITE_OUT_DEF():
    WFOUT_SHORT()
    screen_fadeout(1.0, 255, 255, 255)

def WHITE_OUT_LONG():
    WFOUT_SHORT()
    screen_fadeout(2.0, 255, 255, 255)

def TRANS_IN_RIGHT_DEF():
    fade_color(0.25, 0, 0, 0, 0)
    screen_transin(1, 1.0)

def TRANS_OUT_RIGHT_DEF():
    WFOUT_SHORT()
    screen_transout(1, 1.0)
    fade_color(0.25, 0, 0, 0, 1)

def CURTAIN_OUT():
    set_BG_effect(EFF_107)
    set_BG_effect_trigger(8)
    wait(0.5)

def CURTAIN_IN():
    set_BG_effect(EFF_107)
    set_BG_effect_trigger(9)

def VIS(CID, POS):
    chara_visible(CID, false)
    chara_pos(CID, POS)

def CHARA_SET_0(eye, lip, POS, CID, int):
    chara_visible(CID, false)
    chara_pos(CID, POS)
    chara_face(CID, int)
    eye1(CID, eye)
    lip1(CID, lip)

def CHARA_SET(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    CHARA_FADEIN_DEF(CID)

def CHARA_TYPE(CID, eye2, lip2, POS2, CID2, int2):
    chara_clear(CID)
    c_set_def(eye2, lip2, POS2, CID2, int2)
    chara_fadein(CID2, 0.4)

def CHARA_SET_W(eye, lip, POS, CID, int, int2):
    c_set_def(eye, lip, POS, CID, int)
    chara_face(CID, int2, 1)
    CHARA_FADEIN_DEF(CID)

def CHARA_KAMITE(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    KAMITE_IN_DEF(CID)

def CHARA_KAMITE_SLOW(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    KAMITE_IN_SLOW(CID)

def CHARA_KAMITE_FAST(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    KAMITE_IN_FAST(CID)

def CHARA_KAMITE_VERYFAST(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    KAMITE_IN_VERYFAST(CID)

def CHARA_SHIMOTE(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    SHIMOTE_IN_DEF(CID)

def CHARA_SHIMOTE_SLOW(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    SHIMOTE_IN_SLOW(CID)

def CHARA_SHIMOTE_FAST(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    SHIMOTE_IN_FAST(CID)

def CHARA_SHIMOTE_VERYFAST(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    SHIMOTE_IN_VERYFAST(CID)

def CHARA_TOP(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    TOP_IN_DEF(CID)

def CHARA_BOTTOM(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    BOTTOM_IN_DEF(CID)

def CHARA_BOTTOM_SLOW(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    BOTTOM_IN_SLOW(CID)

def CHARA_BOTTOM_FAST(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    BOTTOM_IN_FAST(CID)

def CHARA_SHIMOTE_ZIG(eye, lip, POS, CID, int):
    c_set_def(eye, lip, POS, CID, int)
    SHIMOTE_IN_ZIG(CID)
    wait(0.7)

def CHARA_BOTTOM_ZIG(eye, lip, POS, CID, int):
    chara_visible(CID, false)
    if(POS == L):
        chara_pos(CID, -200, -50)
    elif(POS == C):
        chara_pos(CID, 0, -50)
    elif(POS == R):
        chara_pos(CID, 200, -50)
    chara_face(CID, int)
    eye1(CID, eye)
    lip1(CID, lip)
    BOTTOM_IN_ZIG(CID)

def CHARA_SET_POS_0(eye, lip, X, Y, CID, int):
    chara_visible(CID, false)
    chara_pos(CID, X, Y)
    chara_face(CID, int)
    eye1(CID, eye)
    lip1(CID, lip)

def CHARA_SET_POS(eye, lip, X, Y, CID, int):
    CHARA_SET_POS_0(eye, lip, X, Y, CID, int)
    CHARA_FADEIN_DEF(CID)

def CHARA_KAMITE_POS(eye, lip, X, Y, CID, int):
    CHARA_SET_POS_0(eye, lip, X, Y, CID, int)
    KAMITE_IN_DEF(CID)

def CHARA_KAMITE_SLOW_POS(eye, lip, X, Y, CID, int):
    CHARA_SET_POS_0(eye, lip, X, Y, CID, int)
    KAMITE_IN_SLOW(CID)

def CHARA_SHIMOTE_POS(eye, lip, X, Y, CID, int):
    CHARA_SET_POS_0(eye, lip, X, Y, CID, int)
    SHIMOTE_IN_DEF(CID)

def CHARA_TOP_SLOW_POS(eye, lip, X, Y, CID, int):
    CHARA_SET_POS_0(eye, lip, X, Y, CID, int)
    TOP_IN_SLOW(CID)

def CHARA_BOTTOM_SLOW_POS(eye, lip, X, Y, CID, int):
    CHARA_SET_POS_0(eye, lip, X, Y, CID, int)
    BOTTOM_IN_SLOW(CID)

def CHARA_KAMITE_SE(eye, lip, POS, CID, int, SE):
    play_sound(SE)
    wait(1.0)
    BGMTUNE_DOWN_0(SE)
    CHARA_KAMITE(eye, lip, POS, CID, int)

def CHARA_KAMITE_SLOW_SE(eye, lip, POS, CID, int, SE):
    play_sound(SE)
    wait(1.0)
    BGMTUNE_DOWN_0(SE)
    CHARA_KAMITE_SLOW(eye, lip, POS, CID, int)

def CHARA_KAMITE_FAST_SE(eye, lip, POS, CID, int, SE):
    play_sound(SE)
    wait(1.0)
    BGMTUNE_DOWN_0(SE)
    CHARA_KAMITE_FAST(eye, lip, POS, CID, int)

def CHARA_KAMITE_VERYFAST_SE(eye, lip, POS, CID, int, SE):
    play_sound(SE)
    wait(1.0)
    BGMTUNE_DOWN_0(SE)
    CHARA_KAMITE_VERYFAST(eye, lip, POS, CID, int)

def CHARA_SHIMOTE_SE(eye, lip, POS, CID, int, SE):
    play_sound(SE)
    wait(1.0)
    BGMTUNE_DOWN_0(SE)
    CHARA_SHIMOTE(eye, lip, POS, CID, int)

def CHARA_SHIMOTE_SLOW_SE(eye, lip, POS, CID, int, SE):
    play_sound(SE)
    wait(1.0)
    BGMTUNE_DOWN_0(SE)
    CHARA_SHIMOTE_SLOW(eye, lip, POS, CID, int)

def CHARA_SHIMOTE_FAST_SE(eye, lip, POS, CID, int, SE):
    play_sound(SE)
    wait(1.0)
    BGMTUNE_DOWN_0(SE)
    CHARA_SHIMOTE_FAST(eye, lip, POS, CID, int)

def CHARA_SHIMOTE_VERYFAST_SE(eye, lip, POS, CID, int, SE):
    play_sound(SE)
    wait(1.0)
    BGMTUNE_DOWN_0(SE)
    CHARA_SHIMOTE_VERYFAST(eye, lip, POS, CID, int)

def CHARA_KAMITE_ZIG_SE(eye, lip, POS, CID, int, SE):
    play_sound(SE)
    wait(0.5)
    c_set_def(eye, lip, POS, CID, int)
    KAMITE_IN_ZIG(CID)
    wait(0.2)
    BGMTUNE_DOWN_0(SE)
    wait(0.5)

def CHARA_LANDING(eye, lip, CID, int):
    play_sound(SE_047)
    CHARA_SET_POS_0(eye, lip, 0, -90, CID, int)
    mnu_move(CID, true, 0.05, 0, 200, 1)
    mnu_move(CID, false, 0.25, 0, -200, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.25)
    mnu_move(CID, true, 0.2, 0, 90, EaseOutCubic)
    cmp_move(CID, 0.2, 0, 90)
    wait(0.2)

def DRG_KAMITE(eye, lip, POS, CID):
    play_sound(SE_136)
    wait(0.3)
    effect_shake_bg(12, 0.1, 0.2, 1)
    wait(0.7)
    effect_shake_bg(12, 0.1, 0.2, 1)
    CHARA_KAMITE_SLOW(eye, lip, POS, CID, 1)
    SEFOUT_DEF()
    wait(1.5)

def DRG_KAMITE_FLY(eye, lip, CID):
    VIS(CID, POS_CENTER)
    chara_face(CID, 1)
    eye1(CID, eye)
    lip1(CID, lip)
    play_sound(SE_040)
    mnu_move(CID, true, 0.01, 190, 200, 1)
    mnu_move(CID, false, 0.6, -190, -210, EaseOutCirc)
    mnu_move(CID, false, 0.6, 0, 0, 1)
    mnu_move(CID, false, 0.2, 0, 10, EaseInSine)
    wait(0.01)
    chara_fadein(CID, 0.25)
    wait(0.35)
    play_sound(SE_133)
    effect_shake_bg(12, 0.2, 0.6, 1)
    SEFOUT_DEF()

def DRG_SHIMOTE(eye, lip, POS, CID):
    play_sound(SE_136)
    wait(0.3)
    effect_shake_bg(12, 0.1, 0.2, 1)
    wait(0.7)
    effect_shake_bg(12, 0.1, 0.2, 1)
    CHARA_SHIMOTE_SLOW(eye, lip, POS, CID, 1)
    SEFOUT_DEF()
    wait(1.5)

def DRG_SHIMOTE_FLY(eye, lip, CID):
    VIS(CID, POS_CENTER)
    chara_face(CID, 1)
    eye1(CID, eye)
    lip1(CID, lip)
    play_sound(SE_040)
    mnu_move(CID, true, 0.01, -190, 200, 1)
    mnu_move(CID, false, 0.6, 190, -210, EaseOutCirc)
    mnu_move(CID, false, 0.6, 0, 0, 1)
    mnu_move(CID, false, 0.2, 0, 10, EaseInSine)
    wait(0.01)
    chara_fadein(CID, 0.25)
    wait(0.35)
    play_sound(SE_133)
    effect_shake_bg(12, 0.2, 0.6, 1)
    SEFOUT_DEF()

def WARP_IN_P(eye, lip, CID, int):
    WFOUT_DEF()
    chara_visible(CID, false)
    chara_face(CID, int)
    eye1(CID, eye)
    lip1(CID, lip)
    wait(0.1)
    set_render_target(CID, 0)
    play_sound(SE_STORY_PROLOGUE_0001)
    set_BG_effect(EFF_002, EFF_SCE_2D_REN_000)
    set_BG_effect_trigger(0, 25)
    wait(2.7)
    NO_EFFECT()
    chara_visible(CID, true)

def WARP_OUT_P(eye, lip, CID, int):
    chara_face(CID, int)
    eye1(CID, eye)
    lip1(CID, lip)
    wait(0.1)
    set_render_target(CID, 0)
    WFOUT_SHORT()
    play_sound(SE_STORY_PROLOGUE_0001)
    set_BG_effect(EFF_002, EFF_SCE_2D_REN_000)
    set_BG_effect_trigger(0, 29)
    wait(0.2)
    chara_clear(CID)
    wait(2.5)
    NO_EFFECT()

def WARP_IN(eye, lip, CID, int):
    WFOUT_DEF()
    chara_visible(CID, false)
    chara_face(CID, int)
    eye1(CID, eye)
    lip1(CID, lip)
    wait(0.1)
    set_render_target(CID, 0)
    play_sound(SE_010)
    set_BG_effect(EFF_002, EFF_SCE_2D_REN_000)
    set_BG_effect_trigger(0, 25)
    wait(2.7)
    NO_EFFECT()
    chara_visible(CID, true)

def WARP_OUT(eye, lip, CID, int):
    chara_face(CID, int)
    eye1(CID, eye)
    lip1(CID, lip)
    wait(0.1)
    set_render_target(CID, 0)
    WFOUT_SHORT()
    play_sound(SE_010)
    set_BG_effect(EFF_002, EFF_SCE_2D_REN_000)
    set_BG_effect_trigger(0, 29)
    wait(0.2)
    chara_clear(CID)
    wait(2.5)
    NO_EFFECT()

def WARP_OUT_EFF(eye, lip, CID, int):
    chara_face(CID, int)
    eye1(CID, eye)
    lip1(CID, lip)
    wait(0.1)
    set_render_target(CID, 0)
    WFOUT_SHORT()
    play_sound(SE_010)
    set_BG_effect(1, 1, EFF_002, EFF_SCE_2D_REN_000)
    set_BG_effect_trigger(2, 2, 0, 29)
    wait(0.2)
    chara_clear(CID)
    wait(2.5)
    set_BG_effect(1, 1, 0, 0)

def CHARA_SET2(eye, lip, CID, int, eye2, lip2, CID2, int2):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_face(CID, int)
    chara_face(CID2, int2)
    eye1(CID, eye)
    eye1(CID2, eye2)
    lip1(CID, lip)
    lip1(CID2, lip2)
    mnu_fade(CID, true, 0.3, 1.0, 1)
    mnu_fade(CID2, true, 0.3, 1.0, 1)
    cmp_fade(CID, 0.3, 1.0)
    cmp_fade(CID2, 0.3, 1.0)
    wait(0.3)
    chara_visible(CID, true)
    chara_visible(CID2, true)

def CHARA_KAMITE2(eye, lip, CID, int, eye2, lip2, CID2, int2):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_face(CID, int)
    chara_face(CID2, int2)
    eye1(CID, eye)
    eye1(CID2, eye2)
    lip1(CID, lip)
    lip1(CID2, lip2)
    KAMITE_IN_DEF(CID)
    KAMITE_IN_DEF(CID2)

def CHARA_SHIMOTE2(eye, lip, CID, int, eye2, lip2, CID2, int2):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_pos(CID, 3)
    chara_pos(CID2, 1)
    chara_face(CID, int)
    chara_face(CID2, int2)
    eye1(CID, eye)
    eye1(CID2, eye2)
    lip1(CID, lip)
    lip1(CID2, lip2)
    SHIMOTE_IN_DEF(CID)
    SHIMOTE_IN_DEF(CID2)

def MONSTER_SET2(CID, CID2):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_pos(CID, 3)
    chara_pos(CID2, 1)
    chara_face(CID, 12)
    chara_face(CID2, 12)
    mnu_fade(CID, true, 0.3, 1.0, 1)
    mnu_fade(CID2, true, 0.3, 1.0, 1)
    cmp_fade(CID, 0.3, 1.0)
    cmp_fade(CID2, 0.3, 1.0)
    chara_visible(CID, true)
    chara_visible(CID2, true)

def MONSTER_SHIMOTE2(CID, CID2):
    WFOUT_DEF()
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_pos(CID, 3)
    chara_pos(CID2, 1)
    SHIMOTE_IN_DEF(CID)
    wait(0.3)
    SHIMOTE_IN_DEF(CID2)

def CHARA_KAMITE2_SE(eye, lip, CID, int, eye2, lip2, CID2, int2, SE):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_face(CID, int)
    chara_face(CID2, int2)
    eye1(CID, eye)
    eye1(CID2, eye2)
    lip1(CID, lip)
    lip1(CID2, lip2)
    play_sound(SE)
    wait(0.5)
    KAMITE_IN_DEF(CID)
    wait(0.3)
    BGMTUNE_DOWN_0(SE)
    KAMITE_IN_DEF(CID2)

def CHARA_SHIMOTE2_SE(eye, lip, CID, int, eye2, lip2, CID2, int2, SE):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_face(CID, int)
    chara_face(CID2, int2)
    eye1(CID, eye)
    eye1(CID2, eye2)
    lip1(CID, lip)
    lip1(CID2, lip2)
    play_sound(SE)
    wait(0.5)
    SHIMOTE_IN_DEF(CID)
    wait(0.3)
    BGMTUNE_DOWN_0(SE)
    SHIMOTE_IN_DEF(CID2)

def CHARA_SET3(eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_pos(CID3, 2)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    eye1(CID, eye)
    eye1(CID2, eye2)
    eye1(CID3, eye3)
    lip1(CID, lip)
    lip1(CID2, lip2)
    lip1(CID3, lip3)
    mnu_fade(CID, true, 0.3, 1.0, 1)
    mnu_fade(CID2, true, 0.3, 1.0, 1)
    mnu_fade(CID3, true, 0.3, 1.0, 1)
    cmp_fade(CID, 0.3, 1.0)
    cmp_fade(CID2, 0.3, 1.0)
    cmp_fade(CID3, 0.3, 1.0)
    wait(0.3)
    chara_visible(CID, true)
    chara_visible(CID2, true)
    chara_visible(CID3, true)

def CHARA_KAMITE3(eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_pos(CID3, 2)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    eye1(CID, eye)
    eye1(CID2, eye2)
    eye1(CID3, eye3)
    lip1(CID, lip)
    lip1(CID2, lip2)
    lip1(CID3, lip3)
    KAMITE_IN_DEF(CID)
    KAMITE_IN_DEF(CID2)
    KAMITE_IN_DEF(CID3)

def CHARA_KAMITE3_VERYFAST(eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_pos(CID3, 2)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    eye1(CID, eye)
    eye1(CID2, eye2)
    eye1(CID3, eye3)
    lip1(CID, lip)
    lip1(CID2, lip2)
    lip1(CID3, lip3)
    KAMITE_IN_VERYFAST(CID)
    KAMITE_IN_VERYFAST(CID2)
    KAMITE_IN_VERYFAST(CID3)

def CHARA_SHIMOTE3(eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_pos(CID3, 2)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    eye1(CID, eye)
    eye1(CID2, eye2)
    eye1(CID3, eye3)
    lip1(CID, lip)
    lip1(CID2, lip2)
    lip1(CID3, lip3)
    SHIMOTE_IN_DEF(CID)
    SHIMOTE_IN_DEF(CID2)
    SHIMOTE_IN_DEF(CID3)

def CHARA_SHIMOTE3_VERYFAST(eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_pos(CID3, 2)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    eye1(CID, eye)
    eye1(CID2, eye2)
    eye1(CID3, eye3)
    lip1(CID, lip)
    lip1(CID2, lip2)
    lip1(CID3, lip3)
    SHIMOTE_IN_VERYFAST(CID)
    SHIMOTE_IN_VERYFAST(CID2)
    SHIMOTE_IN_VERYFAST(CID3)

def MONSTER_SET3_0(CID, CID2, CID3):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_contrast(CID, 0.73, 0)
    chara_saturation(CID, 1.77, 0)
    chara_brightness(CID, 1.02, 0)
    chara_contrast(CID2, 0.73, 0)
    chara_saturation(CID2, 1.77, 0)
    chara_brightness(CID2, 1.02, 0)
    chara_pos(CID, 200, 240)
    chara_pos(CID2, -200, 240)
    chara_pos(CID3, 0, 10)
    chara_face(CID, 12)
    chara_face(CID2, 12)
    chara_face(CID3, 12)
    mnu_scale(CID3, true, 0.01, 1.0, 1.0, EaseOutCubic)
    mnu_scale(CID2, true, 0.01, 0.7, 0.7, EaseOutCubic)
    mnu_scale(CID, true, 0.01, 0.7, 0.7, EaseOutCubic)
    cmp_scale(CID3, 0.01, 1.0, 1.0)
    cmp_scale(CID2, 0.01, 0.7, 0.7)
    cmp_scale(CID, 0.01, 0.7, 0.7)
    wait(0.01)

def MONSTER_SET3(CID, CID2, CID3):
    MONSTER_SET3_0(CID, CID2, CID3)
    mnu_fade(CID, true, 0.3, 1.0, 1)
    mnu_fade(CID2, true, 0.3, 1.0, 1)
    mnu_fade(CID3, true, 0.3, 1.0, 1)
    wait(0.3)
    chara_visible(CID, true)
    chara_visible(CID2, true)
    chara_visible(CID3, true)

def MONSTER_KAMITE3(CID, CID2, CID3):
    WFOUT_DEF()
    MONSTER_SET3_0(CID, CID2, CID3)
    KAMITE_IN_DEF(CID)
    KAMITE_IN_DEF(CID2)
    KAMITE_IN_DEF(CID3)

def MONSTER_SHIMOTE3(CID, CID2, CID3):
    WFOUT_DEF()
    MONSTER_SET3_0(CID, CID2, CID3)
    SHIMOTE_IN_DEF(CID)
    SHIMOTE_IN_DEF(CID2)
    SHIMOTE_IN_DEF(CID3)

def CHARA_KAMITE3_SE(eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3, SE):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_pos(CID3, 2)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    eye1(CID, eye)
    eye1(CID2, eye2)
    eye1(CID3, eye3)
    lip1(CID, lip)
    lip1(CID2, lip2)
    lip1(CID3, lip3)
    play_sound(SE)
    wait(0.5)
    KAMITE_IN_DEF(CID)
    KAMITE_IN_DEF(CID2)
    BGMTUNE_DOWN_0(SE)
    KAMITE_IN_DEF(CID3)

def CHARA_SHIMOTE3_SE(eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3, SE):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_pos(CID3, 2)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    eye1(CID, eye)
    eye1(CID2, eye2)
    eye1(CID3, eye3)
    lip1(CID, lip)
    lip1(CID2, lip2)
    lip1(CID3, lip3)
    play_sound(SE)
    wait(0.5)
    SHIMOTE_IN_DEF(CID)
    SHIMOTE_IN_DEF(CID2)
    BGMTUNE_DOWN_0(SE)
    SHIMOTE_IN_DEF(CID3)

def CHARA_SHIMOTE3_VERYFAST_SE(eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3, SE):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_pos(CID, 1)
    chara_pos(CID2, 3)
    chara_pos(CID3, 2)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    eye1(CID, eye)
    eye1(CID2, eye2)
    eye1(CID3, eye3)
    lip1(CID, lip)
    lip1(CID2, lip2)
    lip1(CID3, lip3)
    play_sound(SE)
    wait(0.5)
    SHIMOTE_IN_VERYFAST(CID)
    SHIMOTE_IN_VERYFAST(CID2)
    BGMTUNE_DOWN_0(SE)
    SHIMOTE_IN_VERYFAST(CID3)

def CHARA_LANDING3(eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    play_sound(SE_047)
    CHARA_SET_POS_0(eye, lip, -200, -90, CID, int)
    mnu_move(CID, true, 0.05, 0, 200, 1)
    mnu_move(CID, false, 0.25, 0, -200, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.25)
    mnu_move(CID, true, 0.2, 0, 90, EaseOutCubic)
    cmp_move(CID, 0.2, 0, 90)
    play_sound(SE_047)
    CHARA_SET_POS_0(eye2, lip2, 200, -90, CID2, int2)
    mnu_move(CID2, true, 0.05, 0, 200, 1)
    mnu_move(CID2, false, 0.25, 0, -200, EaseOutSine)
    wait(0.05)
    chara_fadein(CID2, 0.25)
    mnu_move(CID2, true, 0.2, 0, 90, EaseOutCubic)
    cmp_move(CID2, 0.2, 0, 90)
    play_sound(SE_047)
    CHARA_SET_POS_0(eye3, lip3, 0, -90, CID3, int3)
    mnu_move(CID3, true, 0.05, 0, 200, 1)
    mnu_move(CID3, false, 0.25, 0, -200, EaseOutSine)
    wait(0.05)
    chara_fadein(CID3, 0.25)
    mnu_move(CID3, true, 0.2, 0, 90, EaseOutCubic)
    cmp_move(CID3, 0.2, 0, 90)

def CHARA_FADEIN_DEF(CID):
    chara_fadein(CID, FIN_DEF)

def KAMITE_IN_DEF(CID):
    mnu_move(CID, true, 0.05, 120, 0, 1)
    mnu_move(CID, false, 0.4, -120, 0, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.4)

def SHIMOTE_IN_DEF(CID):
    mnu_move(CID, true, 0.05, -120, 0, 1)
    mnu_move(CID, false, 0.4, 120, 0, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.4)

def KAMITE_IN_SLOW(CID):
    mnu_move(CID, true, 0.05, 120, 0, 1)
    mnu_move(CID, false, 0.6, -120, 0, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.6)

def SHIMOTE_IN_SLOW(CID):
    mnu_move(CID, true, 0.05, -120, 0, 1)
    mnu_move(CID, false, 0.6, 120, 0, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.6)

def KAMITE_IN_FAST(CID):
    mnu_move(CID, true, 0.05, 120, 0, 1)
    mnu_move(CID, false, 0.3, -120, 0, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.3)

def SHIMOTE_IN_FAST(CID):
    mnu_move(CID, true, 0.05, -120, 0, 1)
    mnu_move(CID, false, 0.3, 120, 0, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.3)

def KAMITE_IN_VERYFAST(CID):
    mnu_move(CID, true, 0.01, 120, 0, 1)
    mnu_move(CID, false, 0.2, -120, 0, EaseOutSine)
    wait(0.01)
    chara_fadein(CID, 0.2)

def SHIMOTE_IN_VERYFAST(CID):
    mnu_move(CID, true, 0.01, -120, 0, 1)
    mnu_move(CID, false, 0.2, 120, 0, EaseOutSine)
    wait(0.01)
    chara_fadein(CID, 0.2)

def TOP_IN_DEF(CID):
    mnu_move(CID, true, 0.05, 0, 120, 1)
    mnu_move(CID, false, 0.4, 0, -120, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.4)

def BOTTOM_IN_DEF(CID):
    mnu_move(CID, true, 0.05, 0, -120, 1)
    mnu_move(CID, false, 0.4, 0, 120, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.4)

def TOP_IN_SLOW(CID):
    mnu_move(CID, true, 0.05, 0, 120, 1)
    mnu_move(CID, false, 0.6, 0, -120, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.6)

def BOTTOM_IN_SLOW(CID):
    mnu_move(CID, true, 0.05, 0, -120, 1)
    mnu_move(CID, false, 0.6, 0, 120, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.6)

def TOP_IN_FAST(CID):
    mnu_move(CID, true, 0.05, 0, 120, 1)
    mnu_move(CID, false, 0.3, 0, -120, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.3)

def BOTTOM_IN_FAST(CID):
    mnu_move(CID, true, 0.05, 0, -120, 1)
    mnu_move(CID, false, 0.3, 0, 120, EaseOutSine)
    wait(0.05)
    chara_fadein(CID, 0.3)

def TOP_IN_VERYFAST(CID):
    mnu_move(CID, true, 0.01, 0, 120, 1)
    mnu_move(CID, false, 0.2, 0, -120, EaseOutSine)
    wait(0.01)
    chara_fadein(CID, 0.2)

def BOTTOM_IN_VERYFAST(CID):
    mnu_move(CID, true, 0.01, 0, -120, 1)
    mnu_move(CID, false, 0.2, 0, 120, EaseOutSine)
    wait(0.01)
    chara_fadein(CID, 0.2)

def KAMITE_IN_ZIG(CID):
    mnu_move(CID, true, 0.05, 160, 0, 1)
    mnu_move(CID, false, 0.15, -20, 20, 1)
    mnu_move(CID, false, 0.3, -40, -40, 1)
    mnu_move(CID, false, 0.3, -40, 40, 1)
    mnu_move(CID, false, 0.3, -40, -40, 1)
    mnu_move(CID, false, 0.15, -20, 20, 1)
    cmp_move(CID, 1.25, 0, 0)
    wait(0.05)
    chara_fadein(CID, 0.5)

def SHIMOTE_IN_ZIG(CID):
    mnu_move(CID, true, 0.05, -160, 0, 1)
    mnu_move(CID, false, 0.15, 20, 20, 1)
    mnu_move(CID, false, 0.3, 40, -40, 1)
    mnu_move(CID, false, 0.3, 40, 40, 1)
    mnu_move(CID, false, 0.3, 40, -40, 1)
    mnu_move(CID, false, 0.15, 20, 20, 1)
    cmp_move(CID, 1.25, 0, 0)
    wait(0.05)
    chara_fadein(CID, 0.5)

def BOTTOM_IN_ZIG(CID):
    c_zigzag_h_t(CID)
    chara_fadein(CID, 0.5)

def TOP_IN_ZIG(CID):
    c_zigzag_h_b(CID)
    chara_fadein(CID, 0.5)

def CHARA_FADEOUT_DEF(CID):
    NO_EMO(CID)
    RESET_TEXT()
    chara_fadeout(CID, 0.2)
    RestartAll(CID)

def CHARA_FADEOUT2_DEF(CID, CID2):
    NO_EMO(CID)
    NO_EMO(CID2)
    RESET_TEXT()
    mnu_fade(CID, true, 0.2, 0, 1)
    mnu_fade(CID2, true, 0.2, 0, 1)
    wait(0.2)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    RestartAll(CID)
    RestartAll(CID2)

def CHARA_FADEOUT3_DEF(CID, CID2, CID3):
    NO_EMO(CID)
    NO_EMO(CID2)
    NO_EMO(CID3)
    RESET_TEXT()
    mnu_fade(CID, true, 0.2, 0, 1)
    mnu_fade(CID2, true, 0.2, 0, 1)
    mnu_fade(CID3, true, 0.2, 0, 1)
    wait(0.2)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    RestartAll(CID)
    RestartAll(CID2)
    RestartAll(CID3)

def CHARA_RESET(CID):
    chara_visible(CID, false)
    chara_face(CID, 0)
    RestartAll(CID)

def KAMITE_OUT_DEF(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.4, 120, 0, EaseInSine)
    chara_fadeout(CID, 0.4)
    RestartAll(CID)

def KAMITE_OUT_SLOW(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.8, 120, 0, EaseInSine)
    chara_fadeout(CID, 0.8)
    RestartAll(CID)

def KAMITE_OUT_FAST(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.3, 120, 0, EaseInSine)
    chara_fadeout(CID, 0.3)
    RestartAll(CID)

def SHIMOTE_OUT_DEF(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.4, -120, 0, EaseInSine)
    chara_fadeout(CID, 0.4)
    RestartAll(CID)

def SHIMOTE_OUT_SLOW(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.8, -120, 0, EaseInSine)
    chara_fadeout(CID, 0.8)
    RestartAll(CID)

def SHIMOTE_OUT_FAST(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.3, -120, 0, EaseInSine)
    chara_fadeout(CID, 0.3)
    RestartAll(CID)

def TOP_OUT_DEF(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.4, 0, 120, EaseInSine)
    chara_fadeout(CID, 0.4)
    RestartAll(CID)

def BOTTOM_OUT_DEF(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.4, 0, -120, EaseInSine)
    chara_fadeout(CID, 0.4)
    RestartAll(CID)

def TOP_OUT_SLOW(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.8, 0, 120, EaseInSine)
    chara_fadeout(CID, 0.8)
    RestartAll(CID)

def BOTTOM_OUT_SLOW(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.8, 0, -120, EaseInSine)
    chara_fadeout(CID, 0.8)
    RestartAll(CID)

def TOP_OUT_FAST(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.3, 0, 120, EaseInSine)
    chara_fadeout(CID, 0.3)
    RestartAll(CID)

def BOTTOM_OUT_FAST(CID):
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.3, 0, -120, EaseInSine)
    chara_fadeout(CID, 0.3)
    RestartAll(CID)

def KAMITE_OUT_DEF_SE(CID, SE):
    play_sound(SE)
    KAMITE_OUT_DEF(CID)
    wait(0.5)
    BGMTUNE_DOWN_0(SE)

def KAMITE_OUT_SLOW_SE(CID, SE):
    play_sound(SE)
    KAMITE_OUT_SLOW(CID)
    wait(0.5)
    BGMTUNE_DOWN_0(SE)

def KAMITE_OUT_FAST_SE(CID, SE):
    play_sound(SE)
    KAMITE_OUT_FAST(CID)
    wait(0.5)
    BGMTUNE_DOWN_0(SE)

def SHIMOTE_OUT_DEF_SE(CID, SE):
    play_sound(SE)
    SHIMOTE_OUT_DEF(CID)
    wait(0.5)
    BGMTUNE_DOWN_0(SE)

def SHIMOTE_OUT_SLOW_SE(CID, SE):
    play_sound(SE)
    SHIMOTE_OUT_SLOW(CID)
    wait(0.5)
    BGMTUNE_DOWN_0(SE)

def SHIMOTE_OUT_FAST_SE(CID, SE):
    play_sound(SE)
    SHIMOTE_OUT_FAST(CID)
    wait(0.5)
    BGMTUNE_DOWN_0(SE)

def JUMP_OUT_DEF(CID):
    mnu_move(CID, true, 0.2, 0, -70, EaseOutCubic)
    cmp_move(CID, 0.2, 0, -70)
    wait(0.3)
    play_sound(SE_082)
    NO_EMO(CID)
    RESET_TEXT()
    mnu_move(CID, true, 0.2, 0, 200, EaseInSine)
    wait(0.1)
    chara_fadeout(CID, 0.1)
    RestartAll(CID)

def d_flyaway_r(CID):
    play_sound(SE_041)
    mnu_move(CID, true, 0.4, 30, 50, EaseOutCirc)
    mnu_move(CID, false, 0.2, 10, -30, EaseInCirc)
    mnu_move(CID, false, 0.3, 150, 280, EaseInQuad)
    wait(0.65)
    chara_fadeout(CID, 0.25)

def d_flyaway_l(CID):
    play_sound(SE_041)
    mnu_move(CID, true, 0.1, -30, 50, EaseInSine)
    mnu_move(CID, false, 0.4, -160, 250, EaseOutSine)
    wait(0.25)
    chara_fadeout(CID, 0.25)

def d_flyaway_l_slow(CID):
    play_sound(SE_041)
    mnu_move(CID, true, 0.3, -20, 50, EaseInQuad)
    mnu_move(CID, false, 0.5, -10, -25, EaseOutQuad)
    mnu_move(CID, false, 0.6, -160, 275, EaseInQuad)
    wait(1.1)
    chara_fadeout(CID, 0.3)

def KAMITE_OUT2_DEF(CID, CID2):
    NO_EMO(CID)
    NO_EMO(CID2)
    mnu(CID, true, 0.4, 120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    mnu(CID2, true, 0.4, 120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    wait(0.4)
    chara_visible(CID, false)
    chara_visible(CID2, false)

def KAMITE_OUT2_SLOW(CID, CID2):
    NO_EMO(CID)
    NO_EMO(CID2)
    mnu(CID, true, 0.8, 120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    mnu(CID2, true, 0.8, 120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    wait(0.8)
    chara_visible(CID, false)
    chara_visible(CID2, false)

def KAMITE_OUT2_FAST(CID, CID2):
    NO_EMO(CID)
    NO_EMO(CID2)
    mnu(CID, true, 0.3, 120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    mnu(CID2, true, 0.3, 120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    wait(0.3)
    chara_visible(CID, false)
    chara_visible(CID2, false)

def SHIMOTE_OUT2_DEF(CID, CID2):
    NO_EMO(CID)
    NO_EMO(CID2)
    mnu(CID, true, 0.4, -120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    mnu(CID2, true, 0.4, -120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    wait(0.4)
    chara_visible(CID, false)
    chara_visible(CID2, false)

def SHIMOTE_OUT2_SLOW(CID, CID2):
    NO_EMO(CID)
    NO_EMO(CID2)
    mnu(CID, true, 0.8, -120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    mnu(CID2, true, 0.8, -120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    wait(0.8)
    chara_visible(CID, false)
    chara_visible(CID2, false)

def SHIMOTE_OUT2_FAST(CID, CID2):
    NO_EMO(CID)
    NO_EMO(CID2)
    mnu(CID, true, 0.3, -120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    mnu(CID2, true, 0.3, -120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    wait(0.3)
    chara_visible(CID, false)
    chara_visible(CID2, false)

def KAMITE_OUT2_FAST_SE(CID, CID2, SE):
    play_sound(SE)
    KAMITE_OUT2_FAST(CID, CID2)
    wait(0.5)
    BGMTUNE_DOWN_0(SE)

def SHIMOTE_OUT2_DEF_SE(CID, CID2, SE):
    play_sound(SE)
    SHIMOTE_OUT2_DEF(CID, CID2)
    wait(0.5)
    BGMTUNE_DOWN_0(SE)

def SHIMOTE_OUT2_SLOW_SE(CID, CID2, SE):
    play_sound(SE)
    SHIMOTE_OUT2_SLOW(CID, CID2)
    wait(0.5)
    BGMTUNE_DOWN_0(SE)

def KAMITE_OUT3_DEF(CID, CID2, CID3):
    NO_EMO(CID)
    NO_EMO(CID2)
    NO_EMO(CID3)
    mnu(CID, true, 0.4, 120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    mnu(CID2, true, 0.4, 120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    mnu(CID3, true, 0.4, 120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    wait(0.4)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)

def KAMITE_OUT3_SLOW(CID, CID2, CID3):
    NO_EMO(CID)
    NO_EMO(CID2)
    NO_EMO(CID3)
    mnu(CID, true, 0.8, 120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    mnu(CID2, true, 0.8, 120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    mnu(CID3, true, 0.8, 120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    wait(0.8)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)

def KAMITE_OUT3_FAST(CID, CID2, CID3):
    NO_EMO(CID)
    NO_EMO(CID2)
    NO_EMO(CID3)
    mnu(CID, true, 0.3, 120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    mnu(CID2, true, 0.3, 120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    mnu(CID3, true, 0.3, 120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    wait(0.3)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)

def SHIMOTE_OUT3_DEF(CID, CID2, CID3):
    NO_EMO(CID)
    NO_EMO(CID2)
    NO_EMO(CID3)
    mnu(CID, true, 0.4, -120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    mnu(CID2, true, 0.4, -120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    mnu(CID3, true, 0.4, -120, 0, EaseInSine, 0.4, 1, 1, 0, 0.4, 0, 0, 0.4, 0, 1)
    wait(0.4)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)

def SHIMOTE_OUT3_SLOW(CID, CID2, CID3):
    NO_EMO(CID)
    NO_EMO(CID2)
    NO_EMO(CID3)
    mnu(CID, true, 0.8, -120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    mnu(CID2, true, 0.8, -120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    mnu(CID3, true, 0.8, -120, 0, EaseInSine, 0.8, 1, 1, 0, 0.8, 0, 0, 0.8, 0, 1)
    wait(0.8)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)

def SHIMOTE_OUT3_FAST(CID, CID2, CID3):
    NO_EMO(CID)
    NO_EMO(CID2)
    NO_EMO(CID3)
    mnu(CID, true, 0.3, -120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    mnu(CID2, true, 0.3, -120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    mnu(CID3, true, 0.3, -120, 0, EaseInSine, 0.3, 1, 1, 0, 0.3, 0, 0, 0.3, 0, 1)
    wait(0.3)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)

def c_face(eye, lip, CID, int):
    eye1(CID, eye)
    lip1(CID, lip)
    chara_face(CID, int)

def c_face_w(eye, lip, CID, int, int2):
    c_face(eye, lip, CID, int)
    chara_face(CID, int2, 1)

def SCREEN_FLASH_WHITE_DEF():
    screen_flash(0.04, 255, 255, 255)

def SCREEN_FLASH_RED_DEF():
    screen_flash(0.04, 255, 0, 0)

def NO_EFFECT():
    set_BG_effect(0, 0, 0, 0, 0)

def CHANGE_DRAGON_LUMINE():
    set_BG_effect(EFF_070, EFF_071)
    set_BG_effect_trigger(9, 9)

def CHANGE_DRAGON_LUMINE_SE():
    play_sound(SE_209)
    set_BG_effect(EFF_070, EFF_071)
    set_BG_effect_trigger(8, 8)

def CHANGE_DRAGON_LUMINE_DR():
    set_BG_effect(EFF_072, EFF_073)
    set_BG_effect_trigger(9, 9)

def CHANGE_DRAGON_LUMINE_DR_SE():
    play_sound(SE_209)
    set_BG_effect(EFF_072, EFF_073)
    set_BG_effect_trigger(8, 8)

def CHANGE_DRAGON(CID, CID2, SE):
    NO_EMO(CID)
    WFOUT_SHORT()
    set_BG_effect(EFF_070, EFF_071, EFF_020)
    set_BG_effect_trigger(8, 8, 2)
    play_sound(SE_210)
    wait(0.9)
    fade_color(0.2, 255, 255, 255, 1)
    NO_EFFECT()
    set_BG_effect(EFF_020)
    CHARA_RESET(CID)
    CHARA_SET(M, M, C, CID2, 1)
    set_BG_effect(EFF_020)
    set_BG_effect_trigger(1)
    fade_color(1.5, 255, 255, 255, 0.7)
    set_BG_effect_trigger(1)
    fade_color(1.0, 255, 255, 255, 0.4)
    set_camera_distortion(1, true, EFF_007)
    set_BG_effect(EFF_007)
    set_BG_effect_speed(EFF_007, 0.2)
    set_BG_effect_trigger(8)
    fade_color(0.5, 255, 255, 255, 0.2)
    set_BG_effect_trigger(1)
    fade_color(2.0, 255, 255, 255, 0.0)
    NO_EFFECT()
    play_sound(SE)
    set_BG_effect(EFF_007)
    set_BG_effect_speed(EFF_007, 1.5)
    set_BG_effect_trigger(8)
    effect_shake_bg(12, 0.5, 1.5, 1)
    NO_EFFECT()
    set_camera_distortion(1, false, EFF_007)

def CHANGE_DRAGON_RELEASE(CID, CID2, int):
    WFOUT_SHORT()
    set_BG_effect(EFF_020)
    play_sound(SE_005)
    wait(1.1)
    CHARA_RESET(CID)
    CHARA_SET(M, M, C, CID2, int)
    wait(0.5)

def ARTICLE_STONE(EFF):
    SCREEN_FLASH_WHITE_DEF()
    WFOUT_DEF()
    play_sound(SE_139)
    play_sound(SE_140)
    if(EFF == EFF_022):
        set_BG_effect(0, EFF_025)
        set_BG_effect_pos(EFF_025, 0, 100)
    elif(EFF == EFF_023):
        set_BG_effect(0, EFF_026)
        set_BG_effect_pos(EFF_026, 0, 100)
    fade_color(0.8, 255, 255, 255, 1)
    set_BG_effect(EFF, 1)
    set_BG_effect_pos(EFF, 0, 100)
    fade_color(3.0, 255, 255, 255, 0)
    touch_wait()
    NO_EFFECT()
    SEFOUT_DEF()

def EARTHSHAKE():
    WFOUT_DEF()
    SCREEN_FLASH_WHITE_DEF()
    play_sound(SE_034)
    effect_shake_bg(2, 1, 2)

def EXP_EARTHSHAKE():
    WFOUT_DEF()
    SCREEN_FLASH_WHITE_DEF()
    play_sound(SE_007)
    play_sound(SE_034)
    effect_shake_bg(2, 1, 2)

def THUNDER():
    wait(0.5)
    SCREEN_FLASH_WHITE_DEF()
    wait(0.2)
    SCREEN_FLASH_WHITE_DEF()
    fade_color(0.1, 255, 255, 255, 1)
    play_sound(SE_078)
    fade_color(1.5, 255, 255, 255, 0)
    wait(0.5)

def THUNDER_SHAKE():
    wait(0.5)
    SCREEN_FLASH_WHITE_DEF()
    wait(0.2)
    SCREEN_FLASH_WHITE_DEF()
    fade_color(0.1, 255, 255, 255, 1)
    play_sound(SE_078)
    fade_color(0.8, 255, 255, 255, 0.5)
    play_sound(SE_007)
    fade_color(0.3, 255, 255, 255, 0.125)
    set_volume(0, 2.0, SE_007)
    fade_color(0.1, 255, 255, 255, 0)
    effect_shake_bg(1, 0.5, 1.0)
    wait(0.5)

def TEAR():
    touch_enable(false)
    play_sound(SE_057)
    set_BG_effect(EFF_004)
    set_BG_effect_pos(EFF_004, 0, 100)
    set_BG_effect_trigger(8)
    wait(2.5)
    touch_enable(true)
    touch_wait()
    SEFOUT_DEF()

def HAPPY():
    play_sound(SE_170)
    set_BG_effect(EFF_094)

def KIRA(posX, posY, scaleX, scaleY):
    play_sound(SE_256)
    set_BG_effect(EFF_015)
    set_BG_effect_pos(EFF_015, posX, posY)
    set_BG_effect_scale(EFF_015, scaleX, scaleY)

def SHOUT_0():
    set_BG_effect(EFF_007)
    set_BG_effect_opacity(EFF_007, 0.5)
    set_BG_effect_speed(EFF_007, 1.3)
    set_BG_effect_trigger(9)

def SHOUT_0_EFF():
    set_BG_effect(1, 1, EFF_007)
    set_BG_effect_opacity(EFF_007, 0.5)
    set_BG_effect_speed(EFF_007, 1.3)
    set_BG_effect_trigger(2, 2, 9)

def SHOUT_COM():
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    SHOUT_0()
    effect_shake_bg(12, 0.5, 1.5, 1)

def SHOUT_STOP():
    wait(1.0)
    set_BG_effect_trigger(1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_COM_EFF():
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    SHOUT_0_EFF()
    effect_shake_bg(12, 0.5, 1.5, 1)

def SHOUT_STOP_EFF():
    wait(1.0)
    set_BG_effect_trigger(2, 2, 1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_COM_BG():
    effect_shake_bg(12, 0.5, 1.5, 1)

def SHOUT_STOP_BG():
    wait(1.8)

def SHOUT_COM_BG_EFF():
    effect_shake_bg(12, 0.5, 1.5, 1)

def SHOUT_STOP_BG_EFF():
    wait(1.8)

def SHOUT_BG():
    effect_shake_bg(12, 0.5, 1.5, 1)

def SHOUT_MID_EFF():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_STORY_COMMON_0212)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    set_BG_effect(1, 1, EFF_007)
    set_BG_effect_opacity(EFF_007, 0.5)
    set_BG_effect_speed(EFF_007, 1.3)
    set_BG_effect_trigger(2, 2, 9)
    effect_shake_bg(12, 0.5, 1.5, 1)
    set_BG_effect_trigger(2, 2, 1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_MID():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_STORY_COMMON_0212)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    SHOUT_0()
    effect_shake_bg(12, 0.5, 1.5, 1)
    set_BG_effect_trigger(1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_MER_EFF():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_STORY_COMMON_0214)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    set_BG_effect(1, 1, EFF_007)
    set_BG_effect_opacity(EFF_007, 0.5)
    set_BG_effect_speed(EFF_007, 1.3)
    set_BG_effect_trigger(2, 2, 9)
    effect_shake_bg(12, 0.4, 1.2, 1)
    set_BG_effect_trigger(2, 2, 1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_BRY_EFF():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_STORY_COMMON_0213)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    set_BG_effect(1, 1, EFF_007)
    set_BG_effect_opacity(EFF_007, 0.5)
    set_BG_effect_speed(EFF_007, 1.3)
    set_BG_effect_trigger(2, 2, 9)
    effect_shake_bg(12, 0.4, 1.2, 1)
    set_BG_effect_trigger(2, 2, 1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_BRY():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_STORY_COMMON_0213)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    SHOUT_0()
    effect_shake_bg(12, 0.4, 1.2, 1)
    set_BG_effect_trigger(1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_JUP_EFF():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_STORY_COMMON_0215)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    set_BG_effect(1, 1, EFF_007)
    set_BG_effect_opacity(EFF_007, 0.5)
    set_BG_effect_speed(EFF_007, 1.3)
    set_BG_effect_trigger(8, 8, 9)
    effect_shake_bg(12, 0.4, 1.2, 1)
    set_BG_effect_trigger(2, 2, 1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_JUP():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_STORY_COMMON_0215)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    SHOUT_0()
    effect_shake_bg(12, 0.4, 1.2, 1)
    set_BG_effect_trigger(1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_ZOD():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_STORY_COMMON_0216)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    SHOUT_0()
    effect_shake_bg(12, 0.4, 1.2, 1)
    set_BG_effect_trigger(1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_MON_EFF():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_014)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    set_BG_effect(1, 1, EFF_007)
    set_BG_effect_opacity(EFF_007, 0.5)
    set_BG_effect_speed(EFF_007, 1.3)
    set_BG_effect_trigger(2, 2, 9)
    effect_shake_bg(12, 0.4, 1.2, 1)
    set_BG_effect_trigger(2, 2, 1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def SHOUT_MON():
    WFOUT_DEF()
    wait(0.2)
    play_sound(SE_014)
    set_camera_distortion(cameraType_Chara, true, EFF_007)
    SHOUT_0()
    effect_shake_bg(12, 0.4, 1.2, 1)
    set_BG_effect_trigger(1)
    set_camera_distortion(cameraType_Chara, false, EFF_007)

def CHARA_ATTACK_SWD(CID):
    WFOUT_SHORT()
    play_sound(SE_228)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)

def CHARA_ATTACK_KAT(CID):
    WFOUT_SHORT()
    play_sound(SE_225)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)

def CHARA_ATTACK_DAG(CID):
    WFOUT_SHORT()
    play_sound(SE_224)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)

def CHARA_ATTACK_AXE(CID):
    WFOUT_SHORT()
    play_sound(SE_117)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)

def CHARA_ATTACK_LAN(CID):
    WFOUT_SHORT()
    play_sound(SE_226)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)

def CHARA_ATTACK_BOW(CID):
    WFOUT_SHORT()
    play_sound(SE_222)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)

def CHARA_ATTACK_GUN(CID):
    WFOUT_SHORT()
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)

def CHARA_ATTACK_FIRE(CID):
    WFOUT_SHORT()
    set_BG_effect(EFF_070, EFF_071)
    set_BG_effect_color(EFF_070, 255, 138, 0)
    set_BG_effect_color(EFF_071, 255, 138, 0)
    set_BG_effect_opacity(EFF_070, 0.8)
    set_BG_effect_opacity(EFF_071, 0.8)
    set_BG_effect_trigger(9, 9)
    wait(0.8)
    NO_EFFECT()
    set_BG_effect(EFF_050)
    set_BG_effect_color(EFF_050, 255, 15, 0)
    set_BG_effect_speed(EFF_050, 3)
    play_sound(SE_062)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)
    wait(0.6)
    set_BG_effect(0, 0)

def CHARA_ATTACK_WATER(CID):
    WFOUT_SHORT()
    set_BG_effect(EFF_070, EFF_071)
    set_BG_effect_color(EFF_070, 4, 144, 253)
    set_BG_effect_color(EFF_071, 4, 144, 253)
    set_BG_effect_opacity(EFF_070, 0.8)
    set_BG_effect_opacity(EFF_071, 0.8)
    set_BG_effect_trigger(9, 9)
    wait(0.8)
    NO_EFFECT()
    set_BG_effect(1, 1, EFF_050)
    set_BG_effect_color(EFF_050, 4, 144, 253)
    set_BG_effect_speed(EFF_050, 3)
    play_sound(SE_063)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)
    wait(0.6)
    set_BG_effect(0, 0)

def CHARA_ATTACK_WIND(CID):
    WFOUT_SHORT()
    set_BG_effect(EFF_070, EFF_071)
    set_BG_effect_color(EFF_070, 80, 247, 28)
    set_BG_effect_color(EFF_071, 80, 247, 28)
    set_BG_effect_opacity(EFF_070, 0.8)
    set_BG_effect_opacity(EFF_071, 0.8)
    set_BG_effect_trigger(9, 9)
    wait(0.8)
    NO_EFFECT()
    set_BG_effect(EFF_050)
    set_BG_effect_color(EFF_050, 198, 251, 40)
    set_BG_effect_speed(EFF_050, 3)
    play_sound(SE_064)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)
    wait(0.6)
    set_BG_effect(0, 0)

def CHARA_ATTACK_LIGHT(CID):
    WFOUT_SHORT()
    set_BG_effect(EFF_070, EFF_071)
    set_BG_effect_opacity(EFF_070, 0.8)
    set_BG_effect_opacity(EFF_071, 0.8)
    set_BG_effect_trigger(9, 9)
    wait(0.8)
    NO_EFFECT()
    set_BG_effect(EFF_108)
    set_BG_effect_pos(EFF_108, 0, -100)
    set_BG_effect_speed(EFF_108, 2)
    play_sound(SE_061)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)
    wait(0.1)
    set_BG_effect_opacity(EFF_108, 0, 0.5)
    wait(0.5)
    set_BG_effect(0, 0)

def CHARA_ATTACK_DARK(CID):
    WFOUT_SHORT()
    set_BG_effect(EFF_070, EFF_071)
    set_BG_effect_color(EFF_070, 79, 0, 225)
    set_BG_effect_color(EFF_071, 79, 0, 225)
    set_BG_effect_opacity(EFF_070, 0.8)
    set_BG_effect_opacity(EFF_071, 0.8)
    set_BG_effect_trigger(9, 9)
    wait(0.8)
    set_BG_effect_opacity(EFF_070, 0, 0.3)
    set_BG_effect_opacity(EFF_071, 0, 0.3)
    set_BG_effect(1, 1, EFF_046)
    set_BG_effect_speed(EFF_046, 1.5)
    play_sound(SE_060)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)
    wait(0.6)
    set_BG_effect(0, 0)

def CHARA_ATTACK_MC_009(CID):
    WFOUT_SHORT()
    play_sound(SE_043)
    set_BG_effect(EFF_010, EFF_011, EFF_046)
    play_sound(SE_044)
    set_camera_distortion(1, true, EFF_007)
    set_BG_effect(1, 1, EFF_046, EFF_007)
    set_BG_effect_color(EFF_046, 46, 9, 56)
    set_BG_effect_color(EFF_007, 178, 120, 221)
    set_BG_effect_opacity(EFF_046, 2.0)
    set_BG_effect_opacity(EFF_007, 1.1)
    set_BG_effect_speed(EFF_046, 2.5)
    set_BG_effect_speed(EFF_007, 1.2)
    set_BG_effect_trigger(9, 9, 1, 8)
    wait(0.5)
    set_BG_effect_trigger(2, 2, 1, 1)
    set_camera_distortion(1, false, EFF_007)

def CHARA_ATTACK_DARK2_EFF(CID):
    WFOUT_SHORT()
    play_sound(SE_043)
    set_BG_effect(1, 1)
    play_sound(SE_044)
    set_camera_distortion(1, true, EFF_007)
    set_BG_effect(1, 1, EFF_007)
    set_BG_effect_color(EFF_007, 178, 120, 221)
    set_BG_effect_opacity(EFF_007, 1.1)
    set_BG_effect_speed(EFF_007, 1.2)
    set_BG_effect_trigger(2, 2, 9)
    wait(0.5)
    set_BG_effect_trigger(2, 2, 1)
    set_camera_distortion(1, false, EFF_007)

def CHARA_ATTACK_DARK2(CID):
    WFOUT_SHORT()
    play_sound(SE_043)
    play_sound(SE_044)
    set_camera_distortion(1, true, EFF_007)
    set_BG_effect(EFF_007)
    set_BG_effect_color(EFF_007, 178, 120, 221)
    set_BG_effect_opacity(EFF_007, 1.1)
    set_BG_effect_speed(EFF_007, 1.2)
    set_BG_effect_trigger(9)
    wait(0.5)
    set_BG_effect_trigger(1)
    set_camera_distortion(1, false, EFF_007)

def CHARA_ATTACK_ZETH(CID):
    WFOUT_SHORT()
    set_BG_effect(EFF_025)
    set_BG_effect_speed(EFF_025, 3)
    wait(0.3)
    play_sound(SE_061)
    set_camera_distortion(1, true, EFF_007)
    set_BG_effect(1, EFF_007)
    set_BG_effect_opacity(EFF_007, 0.6)
    set_BG_effect_speed(EFF_007, 1.0)
    set_BG_effect_trigger(2, 9)
    wait(0.3)
    set_BG_effect_trigger(2, 1)
    set_BG_effect(0, 0)
    set_camera_distortion(1, false, EFF_007)

def CHARA_ATTACK_MON(CID):
    WFOUT_SHORT()
    play_sound(SE_099)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)

def CHARA_ATTACK_HIT(CID):
    WFOUT_SHORT()
    play_sound(SE_117)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)

def CHARA_ATTACK_DRG(CID):
    WFOUT_SHORT()
    play_sound(SE_129)
    set_camera_distortion(1, true, EFF_007)
    set_BG_effect(EFF_007)
    set_BG_effect_opacity(EFF_007, 0.6)
    set_BG_effect_trigger(9)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)
    wait(0.3)
    NO_EFFECT()
    set_camera_distortion(1, false, EFF_007)

def CHARA_ATTACK_DRG_EFF(CID):
    WFOUT_SHORT()
    play_sound(SE_129)
    set_camera_distortion(1, true, EFF_007)
    set_BG_effect(1, 1, EFF_007)
    set_BG_effect_opacity(EFF_007, 0.6)
    set_BG_effect_trigger(2, 2, 9)
    mnu_scale(CID, true, 0.15, 1.35, 1.35, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseOutCubic)
    cmp_scale(CID, 0.3, 1, 1)
    wait(0.3)
    set_BG_effect(1, 1, 0)
    set_camera_distortion(1, false, EFF_007)

def CHARA_BEAT_SWD(eye, lip, CID, int):
    WFOUT_SHORT()
    CHARA_BEAT_SWD_BEFORE(eye, lip, CID, int)
    wait(0.3)
    CHARA_BEAT_AFTER_0(CID)

def CHARA_BEAT_WIND(eye, lip, CID, int):
    WFOUT_SHORT()
    CHARA_BEAT_WIND_BEFORE(eye, lip, CID, int)
    wait(0.3)
    CHARA_BEAT_AFTER_0(CID)

def MONSTER_BEAT_SWD(CID):
    WFOUT_SHORT()
    CHARA_SET(M, M, C, CID, 1)
    set_BG_effect(EFF_090)
    wait(0.1)
    play_sound(SE_233)
    c_swing2_h_fast(CID)
    wait(0.55)
    play_sound(SE_205)
    MONSTER_BEAT_AFTER_0(CID)

def MONSTER_BEAT_KAT(CID):
    WFOUT_SHORT()
    CHARA_SET(M, M, C, CID, 1)
    set_BG_effect(EFF_090)
    wait(0.1)
    play_sound(SE_234)
    c_swing2_h_fast(CID)
    wait(0.55)
    play_sound(SE_205)
    MONSTER_BEAT_AFTER_0(CID)

def MONSTER_BEAT_DAG(CID):
    WFOUT_SHORT()
    CHARA_SET(M, M, C, CID, 1)
    set_BG_effect(EFF_090)
    wait(0.1)
    play_sound(SE_236)
    c_swing2_h_fast(CID)
    wait(0.55)
    play_sound(SE_205)
    MONSTER_BEAT_AFTER_0(CID)

def MONSTER_BEAT_AXE(CID):
    WFOUT_SHORT()
    CHARA_SET(M, M, C, CID, 1)
    set_BG_effect(EFF_093)
    wait(0.1)
    play_sound(SE_116)
    c_swing2_h_fast(CID)
    wait(0.55)
    play_sound(SE_205)
    MONSTER_BEAT_AFTER_0(CID)

def MONSTER_BEAT_LAN(CID):
    WFOUT_SHORT()
    CHARA_SET(M, M, C, CID, 1)
    set_BG_effect(EFF_090)
    wait(0.1)
    play_sound(SE_238)
    c_swing2_h_fast(CID)
    wait(0.55)
    play_sound(SE_205)
    MONSTER_BEAT_AFTER_0(CID)

def MONSTER_BEAT_BOW(CID):
    WFOUT_SHORT()
    CHARA_SET(M, M, C, CID, 1)
    set_BG_effect(EFF_092)
    set_BG_effect_trigger(8)
    set_BG_effect_speed(EFF_092, 1.5)
    wait(0.3)
    c_swing2_h_fast(CID)
    play_sound(SE_239)
    wait(0.55)
    play_sound(SE_205)
    MONSTER_BEAT_AFTER_0(CID)

def MONSTER_BEAT_LIGHT(CID):
    WFOUT_SHORT()
    CHARA_SET(M, M, C, CID, 1)
    play_sound(SE_244)
    wait(0.3)
    set_BG_effect(EFF_038)
    wait(0.2)
    c_swing2_h_fast(CID)
    wait(0.55)
    play_sound(SE_205)
    MONSTER_BEAT_AFTER_0(CID)

def MONSTER_BEAT_DARK(CID):
    WFOUT_SHORT()
    CHARA_SET(M, M, C, CID, 1)
    play_sound(SE_245)
    wait(0.3)
    set_BG_effect(EFF_039)
    wait(0.2)
    c_swing2_h_fast(CID)
    wait(0.55)
    play_sound(SE_205)
    MONSTER_BEAT_AFTER_0(CID)

def MONSTER_BEAT_HIT(CID):
    WFOUT_SHORT()
    CHARA_SET(M, M, C, CID, 1)
    set_BG_effect(EFF_001)
    wait(0.05)
    play_sound(SE_230)
    wait(0.15)
    c_swing2_h_fast(CID)
    wait(0.25)
    play_sound(SE_205)
    MONSTER_BEAT_AFTER_0(CID)

def CHARA_BEAT_SWD_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_SWD_BEFORE_IN(CID)

def CHARA_BEAT_KAT_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_KAT_BEFORE_IN(CID)

def CHARA_BEAT_DAG_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_DAG_BEFORE_IN(CID)

def CHARA_BEAT_AXE_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_AXE_BEFORE_IN(CID)

def CHARA_BEAT_LAN_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_LAN_BEFORE_IN(CID)

def CHARA_BEAT_BOW_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_BOW_BEFORE_IN(CID)

def CHARA_BEAT_FIRE_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_FIRE_BEFORE_IN(CID)

def CHARA_BEAT_WATER_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_WATER_BEFORE_IN(CID)

def CHARA_BEAT_WIND_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_WIND_BEFORE_IN(CID)

def CHARA_BEAT_LIGHT_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_LIGHT_BEFORE_IN(CID)

def CHARA_BEAT_DARK_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_DARK_BEFORE_IN(CID)

def CHARA_BEAT_DARK2_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    set_BG_effect(EFF_040)
    wait(0.2)
    play_sound(SE_044)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_HIT_BEFORE(eye, lip, CID, int):
    CHARA_SET(eye, lip, C, CID, int)
    CHARA_BEAT_HIT_BEFORE_IN(CID)

def CHARA_BEAT_SWD_BEFORE_IN(CID):
    set_BG_effect(EFF_090)
    wait(0.1)
    play_sound(SE_233)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_SWD2_BEFORE_IN(CID):
    set_BG_effect(EFF_089)
    wait(0.1)
    play_sound(SE_233)
    wait(0.15)
    play_sound(SE_233)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_KAT_BEFORE_IN(CID):
    set_BG_effect(EFF_090)
    wait(0.1)
    play_sound(SE_234)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_KAT2_BEFORE_IN(CID):
    set_BG_effect(EFF_089)
    wait(0.1)
    play_sound(SE_234)
    wait(0.15)
    play_sound(SE_234)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_DAG_BEFORE_IN(CID):
    set_BG_effect(EFF_090)
    wait(0.1)
    play_sound(SE_236)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_DAG2_BEFORE_IN(CID):
    set_BG_effect(EFF_089)
    wait(0.1)
    play_sound(SE_236)
    wait(0.15)
    play_sound(SE_236)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_AXE_BEFORE_IN(CID):
    set_BG_effect(EFF_093)
    wait(0.1)
    play_sound(SE_116)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_LAN_BEFORE_IN(CID):
    set_BG_effect(EFF_090)
    wait(0.1)
    play_sound(SE_238)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_LAN2_BEFORE_IN(CID):
    set_BG_effect(EFF_089)
    wait(0.1)
    play_sound(SE_238)
    wait(0.15)
    play_sound(SE_238)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_BOW_BEFORE_IN(CID):
    set_BG_effect(EFF_092)
    set_BG_effect_trigger(8)
    set_BG_effect_speed(EFF_092, 1.5)
    wait(0.3)
    c_swing2_h_fast(CID)
    play_sound(SE_239)
    wait(0.25)

def CHARA_BEAT_FIRE_BEFORE_IN(CID):
    play_sound(SE_241)
    wait(0.3)
    set_BG_effect(EFF_035)
    wait(0.2)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_WATER_BEFORE_IN(CID):
    play_sound(SE_243)
    wait(0.3)
    set_BG_effect(EFF_036)
    wait(0.2)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_WIND_BEFORE_IN(CID):
    play_sound(SE_242)
    wait(0.3)
    set_BG_effect(EFF_037)
    wait(0.2)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT3_WIND_BEFORE_IN(CID, int, CID2, int2, CID3, int3):
    set_BG_effect(EFF_061)
    set_BG_effect_speed(EFF_061, 2.0)
    wait(0.05)
    play_sound(SE_064)
    wait(0.15)
    chara_face(CID, int)
    chara_face(CID2, int2)
    chara_face(CID3, int3)
    chara_shake_h(CID, 2, true)
    chara_shake_h(CID2, 2, true)
    chara_shake_h(CID3, 2, true)
    wait(0.7)
    chara_shake_h(CID, 2, false)
    chara_shake_h(CID2, 2, false)
    chara_shake_h(CID3, 2, false)

def CHARA_BEAT_LIGHT_BEFORE_IN(CID):
    play_sound(SE_244)
    wait(0.3)
    set_BG_effect(EFF_038)
    wait(0.2)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_DARK_BEFORE_IN(CID):
    play_sound(SE_245)
    wait(0.3)
    set_BG_effect(EFF_039)
    wait(0.2)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_DARK2_BEFORE_IN(CID):
    set_BG_effect(EFF_040)
    wait(0.2)
    play_sound(SE_044)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_DARK3_BEFORE_IN(CID):
    set_BG_effect(1, 1, EFF_020)
    set_BG_effect_color(EFF_020, 213, 0, 255, 1)
    set_BG_effect_speed(EFF_020, 0.8)
    wait(1.0)
    play_sound(SE_044)
    wait(0.1)

def CHARA_BEAT_HIT_BEFORE_IN(CID):
    set_BG_effect(EFF_001)
    wait(0.05)
    play_sound(SE_230)
    wait(0.15)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_HIT_BEFORE_IN_EFF(CID):
    set_BG_effect(1, 1, EFF_001)
    wait(0.05)
    play_sound(SE_230)
    wait(0.15)
    c_swing2_h_fast(CID)
    wait(0.25)

def BODYBLOW_BEFORE(CID):
    set_BG_effect(0, 0, 0, EFF_091)
    play_sound(SE_232)
    wait(0.1)
    mnu_move(CID, true, 0.2, 0, 180, EaseOutQuint)
    mnu_move(CID, false, 0.02, 0, 0, 1)
    mnu_move(CID, false, 0.2, 0, -180, EaseInQuint)
    cmp_move(CID, 0.42, 0, 0)

def CHARA_BEAT3_BEFORE_IN(WEAPON, eye, lip, CID, int, eye2, lip2, CID2, int2, eye3, lip3, CID3, int3):
    if(WEAPON == BOW):
        set_BG_effect(EFF_092)
        set_BG_effect_trigger(8)
        set_BG_effect_speed(EFF_092, 1.5)
        wait(0.15)
        play_sound(SE_239)
        set_BG_effect(1, EFF_001)
        set_BG_effect_pos(EFF_001, -160, 50, 0, 1)
        set_BG_effect_speed(EFF_001, 1.5)
        wait(0.15)
        play_sound(SE_239)
        NO_EFFECT()
        set_BG_effect(EFF_001)
        set_BG_effect_pos(EFF_001, 160, 50, 0, 1)
        set_BG_effect_speed(EFF_001, 1.5)
        wait(0.15)
    elif(WEAPON == AXE):
        set_BG_effect(EFF_090, EFF_001)
        set_BG_effect_speed(EFF_090, 0.75)
        set_BG_effect_scale(EFF_090, 2.0, 1.5)
        set_BG_effect_pos(EFF_090, 150, 0)
        set_BG_effect_pos(EFF_001, 150, 50)
        play_sound(SE_116)
        stop_se(0.1)
        wait(0.15)
        play_sound(SE_116)
        set_BG_effect(1, 0, EFF_001)
        set_BG_effect_pos(EFF_001, 0, 0)
        stop_se(0.1)
        wait(0.15)
        play_sound(SE_116)
        set_BG_effect(1, 0, 0, EFF_001)
        set_BG_effect_pos(EFF_001, -150, -50)
        wait(0.15)
    elif(WEAPON == WIND):
        set_BG_effect(EFF_061)
        set_BG_effect_speed(EFF_061, 2.0)
        wait(0.05)
        play_sound(SE_064)
        wait(0.15)
    if(WEAPON == WIND):
        c_face(eye, lip, CID, int)
        c_face(eye2, lip2, CID2, int2)
        c_face(eye3, lip3, CID3, int3)
        chara_shake_h(CID, 2, true)
        chara_shake_h(CID2, 2, true)
        chara_shake_h(CID3, 2, true)
        wait(0.7)
        chara_shake_h(CID, 2, false)
        chara_shake_h(CID2, 2, false)
        chara_shake_h(CID3, 2, false)
    else:
        c_face(eye, lip, CID, int)
        c_face(eye2, lip2, CID2, int2)
        c_face(eye3, lip3, CID3, int3)
        c_swing2_h_fast(CID)
        c_swing2_h_fast(CID2)
        c_swing2_h_fast(CID3)

def MONSTER_BEAT3_BEFORE_IN(WEAPON, CID, CID2, CID3):
    if(WEAPON == BOW):
        play_sound(SE_239)
        set_BG_effect(EFF_092)
        set_BG_effect_trigger(8)
        set_BG_effect_speed(EFF_092, 1.5)
        wait(0.15)
        play_sound(SE_239)
        set_BG_effect(1, EFF_001)
        set_BG_effect_pos(EFF_001, 200, 150)
        set_BG_effect_speed(EFF_001, 1.5)
        set_BG_effect_scale(EFF_001, 0.8, 0.8)
        wait(0.15)
        play_sound(SE_239)
        NO_EFFECT()
        set_BG_effect(EFF_001)
        set_BG_effect_pos(EFF_001, -200, 150)
        set_BG_effect_speed(EFF_001, 1.5)
        set_BG_effect_scale(EFF_001, 0.8, 0.8)
        wait(0.15)
    elif(WEAPON == AXE):
        play_sound(SE_116)
        set_BG_effect(EFF_093)
        wait(0.15)
        play_sound(SE_116)
        set_BG_effect(1, EFF_001)
        set_BG_effect_pos(EFF_001, 200, 150)
        set_BG_effect_speed(EFF_001, 1.5)
        set_BG_effect_scale(EFF_001, 0.8, 0.8)
        wait(0.15)
        play_sound(SE_116)
        NO_EFFECT()
        set_BG_effect(EFF_001)
        set_BG_effect_pos(EFF_001, -200, 150)
        set_BG_effect_speed(EFF_001, 1.5)
        set_BG_effect_scale(EFF_001, 0.8, 0.8)
        wait(0.15)
        if(WEAPON == WATER):
            play_sound(SE_243)
            wait(0.3)
            set_BG_effect(EFF_036)
            wait(0.2)
    elif(WEAPON == WIND):
        set_BG_effect(EFF_061)
        set_BG_effect_speed(EFF_061, 2.0)
        wait(0.05)
        play_sound(SE_064)
        wait(0.15)
    if(WEAPON == WIND):
        chara_shake_h(CID, 2, true)
        chara_shake_h(CID2, 2, true)
        chara_shake_h(CID3, 2, true)
        wait(0.7)
        chara_shake_h(CID, 2, false)
        chara_shake_h(CID2, 2, false)
        chara_shake_h(CID3, 2, false)
    else:
        c_swing2_h_fast(CID)
        c_swing2_h_fast(CID2)
        c_swing2_h_fast(CID3)

def MONSTER_BEAT_AFTER(CID):
    WFOUT_SHORT()
    MONSTER_BEAT_AFTER_0(CID)

def MONSTER_BEAT2_AFTER(CID, CID2):
    WFOUT_SHORT()
    mnu(CID, true, 0.6, 0, -150, EaseOutQuint, 0.6, 1, 1, 1, 0.6, 0, 1, 0.6, 0, 1)
    mnu(CID2, true, 0.6, 0, -150, EaseOutQuint, 0.6, 1, 1, 1, 0.6, 0, 1, 0.6, 0, 1)
    wait(0.6)
    play_sound(SE_262)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    effect_shake_bg(12, 0.1, 0.2, 1)
    wait(0.5)
    RestartAll(CID)
    RestartAll(CID2)

def MONSTER_BEAT3_AFTER(CID, CID2, CID3):
    WFOUT_SHORT()
    mnu(CID, true, 0.6, 0, -150, EaseOutQuint, 0.6, 0.7, 0.7, 1, 0.6, 0, 1, 0.6, 0, 1)
    mnu(CID2, true, 0.6, 0, -150, EaseOutQuint, 0.6, 0.7, 0.7, 1, 0.6, 0, 1, 0.6, 0, 1)
    mnu(CID3, true, 0.6, 0, -150, EaseOutQuint, 0.6, 1.0, 1.0, 1, 0.6, 0, 1, 0.6, 0, 1)
    wait(0.6)
    play_sound(SE_262)
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    effect_shake_bg(12, 0.1, 0.2, 1)
    wait(0.5)
    RestartAll(CID)
    RestartAll(CID2)
    RestartAll(CID3)

def CHARA_BEAT_AFTER(CID):
    WFOUT_SHORT()
    CHARA_BEAT_AFTER_0(CID)

def CHARA_BEAT3_AFTER(CID, CID2, CID3):
    WFOUT_SHORT()
    mnu(CID3, true, 0.6, 0, -150, EaseOutQuint, 0.6, 1, 1, 1, 0.6, 0, 1, 0.6, 0, 1)
    mnu(CID2, true, 0.6, 0, -150, EaseOutQuint, 0.6, 1, 1, 1, 0.6, 0, 1, 0.6, 0, 1)
    mnu(CID, true, 0.6, 0, -150, EaseOutQuint, 0.6, 1, 1, 1, 0.6, 0, 1, 0.6, 0, 1)
    wait(0.6)
    chara_visible(CID3, false)
    chara_face(CID3, 0)
    chara_visible(CID2, false)
    chara_face(CID2, 0)
    chara_visible(CID, false)
    chara_face(CID, 0)
    play_sound(SE_065)
    effect_shake_bg(12, 0.1, 0.2, 1)
    wait(0.5)
    RestartAll(CID)
    RestartAll(CID2)
    RestartAll(CID3)

def CHARA_BEAT_AFTER_0(CID):
    mnu_move(CID, true, 0.6, 0, -150, EaseOutQuint)
    chara_fadeout(CID, 0.6)
    play_sound(SE_065)
    effect_shake_bg(12, 0.1, 0.2, 1)
    wait(0.5)
    RestartAll(CID)

def MONSTER_BEAT_AFTER_0(CID):
    mnu_move(CID, true, 0.6, 0, -150, EaseOutQuint)
    chara_fadeout(CID, 0.6)
    play_sound(SE_262)
    effect_shake_bg(12, 0.1, 0.2, 1)
    wait(0.5)
    RestartAll(CID)

def GUARD_KNIFE(CID):
    SCREEN_FLASH_WHITE_DEF()
    set_BG_effect(EFF_089)
    play_sound(SE_013)
    c_swing_h_mid(CID)
    wait(0.3)
    play_sound(SE_013)
    wait(0.8)

def REPEL_KNIFE(CID, int):
    SCREEN_FLASH_WHITE_DEF()
    set_BG_effect(EFF_089)
    play_sound(SE_013)
    c_swing_h_mid(CID)
    wait(0.3)
    play_sound(SE_013)
    play_sound(SE_047)
    c_push_r(CID)
    wait(0.9)
    play_sound(SE_066)
    chara_face(CID, int)
    wait(0.8)

def MAGIC_CURE_BEFORE():
    play_sound(SE_122)
    fade_color(1.0, 255, 255, 255, 1)

def MAGIC_CURE_AFTER():
    set_BG_effect(EFF_050)
    fade_color(1.0, 255, 255, 255, 0)

def MAGIC_CURE():
    MAGIC_CURE_BEFORE()
    MAGIC_CURE_AFTER()

def MAGIC_CURE_CH(eye2, lip2, CID, CID2, int):
    WFOUT_DEF()
    MAGIC_CURE_BEFORE()
    CHARA_RESET(CID)
    CHARA_SET(eye2, lip2, C, CID2, int)
    MAGIC_CURE_AFTER()
    wait(0.8)

def AURA_DARK_SE():
    set_BG_effect(EFF_010, EFF_011)
    set_BG_effect_trigger(8, 8)
    play_sound(SE_031)

def AURA_DARK():
    set_BG_effect(EFF_010, EFF_011)
    set_BG_effect_trigger(9, 8)

def AURA_DARK_POS_SE(X, Y):
    set_BG_effect(EFF_010, EFF_011)
    set_BG_effect_pos(EFF_010, X, Y)
    set_BG_effect_pos(EFF_011, X, Y)
    set_BG_effect_trigger(8, 8)
    play_sound(SE_031)

def AURA_DARK_POS(X, Y):
    set_BG_effect(EFF_010, EFF_011)
    set_BG_effect_pos(EFF_010, X, Y)
    set_BG_effect_pos(EFF_011, X, Y)
    set_BG_effect_trigger(9, 8)

def CHARA_EMO(CID, EID, FID):
    if(EID == 1):
        chara_emotion(CID, EID, FID, 30.0, 50.0)
    elif(EID == 2):
        chara_emotion(CID, EID, FID, 0.0, 10.0)
    elif(EID == 3):
        chara_emotion(CID, EID, FID, -250.0, 80.0)
    elif(EID == 4):
        chara_emotion(CID, EID, FID, -250.0, 80.0)
    elif(EID == 5):
        chara_emotion(CID, EID, FID, -260.0, 30.0)
    elif(EID == 6):
        chara_emotion(CID, EID, FID, -260.0, 30.0)
    elif(EID == 7):
        chara_emotion(CID, EID, FID, -220.0, 20.0)
    elif(EID == 8):
        chara_emotion(CID, EID, FID, -210.0, 30.0)
    elif(EID == 9):
        chara_emotion(CID, EID, FID, -260.0, 0.0)
    elif(EID == 10):
        chara_emotion(CID, EID, FID, -250.0, 60.0)
    else:
        chara_emotion(CID, EID, FID, 0.0, 0.0)

def ASE_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 1, 0)
    play_sound(SE_IN_EMOTION_0001)

def ASE_jump(CID):
    NO_EMO(CID)
    ASE_EMO(CID)
    c_jump(CID)

def WARAI_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 2, 0)
    play_sound(SE_IN_EMOTION_0002)

def WARAI_jump(CID):
    NO_EMO(CID)
    WARAI_EMO(CID)
    c_jump(CID)

def ONPU_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 3, 0)
    play_sound(SE_IN_EMOTION_0003)

def ONPU_jump(CID):
    NO_EMO(CID)
    ONPU_EMO(CID)
    c_jump(CID)

def IKARI_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 4, 0)
    play_sound(SE_IN_EMOTION_0004)

def IKARI_jump(CID):
    NO_EMO(CID)
    IKARI_EMO(CID)
    c_jump(CID)

def ODOROKI_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 5, 0)
    play_sound(SE_IN_EMOTION_0005)

def ODOROKI_jump(CID):
    NO_EMO(CID)
    ODOROKI_EMO(CID)
    c_jump(CID)

def HATENA_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 6, 0)
    play_sound(SE_IN_EMOTION_0006)

def HATENA_jump(CID):
    NO_EMO(CID)
    HATENA_EMO(CID)
    c_jump(CID)

def MOYA_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 7, 0)
    play_sound(SE_IN_EMOTION_0007)

def ZZZ_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 8, 0)
    play_sound(SE_IN_EMOTION_0008)

def HIRAMEKI_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 9, 0)
    play_sound(SE_IN_EMOTION_0009)

def HIRAMEKI_jump(CID):
    NO_EMO(CID)
    HIRAMEKI_EMO(CID)
    c_jump(CID)

def HEART_EMO(CID):
    NO_EMO(CID)
    CHARA_EMO(CID, 10, 0)
    play_sound(SE_IN_EMOTION_0010)

def HEART_jump(CID):
    NO_EMO(CID)
    HEART_EMO(CID)
    c_jump(CID)

def NO_EMO(CID):
    chara_emotion(CID, 0)

def YORU_LIGHT(CID):
    chara_color(CID, 0, 3, 44, 122, 156, 1, -0.25, 0.67)
    wait(0)

def YORU_LIGHT_0021(CID):
    chara_color(CID, 0, 2, 238, 255, 255, 1, 0.12, 0.7)
    chara_color(CID, 0, 3, 99, 182, 218, 1, 0.12, 0.7)
    chara_contrast(CID, 1)
    chara_saturation(CID, 1.05)
    chara_brightness(CID, 1.03)
    wait(0)

def KURONUKI(CID):
    chara_brightness(CID, 0)
    wait(0)

def CHARA_UNCOLOR(CID):
    chara_color(CID, 0, TYPE_COLOR, 255, 255, 255)
    chara_color(CID, 0, TYPE_COLOR_TOP, 255, 255, 255)
    chara_color(CID, 0, TYPE_COLOR_BOTTOM, 255, 255, 255)
    chara_color(CID, 0, TYPE_COLOR_LASTMUL, 255, 255, 255)
    chara_contrast(CID, 1)
    chara_saturation(CID, 1)
    chara_brightness(CID, 1)
    wait(0)

def mnu(CID, isNewAct, moveSec, moveX, moveY, moveEase, scaleSec, scaleX, scaleY, scaleEase, rotateSec, rotate, rotateEase, fadeSec, fade, fadeEase):
    chara_act_manual(CID, isNewAct, moveSec, moveX, moveY, moveEase, scaleSec, scaleX, scaleY, scaleEase, rotateSec, rotate, rotateEase, fadeSec, fade, fadeEase)

def mnu_move(CID, isNewAct, moveSec, moveX, moveY, moveEase):
    chara_act_manual(CID, isNewAct, moveSec, moveX, moveY, moveEase)

def mnu_scale(CID, isNewAct, scaleSec, scaleX, scaleY, scaleEase):
    chara_act_manual(CID, isNewAct, 0, 0, 0, 0, scaleSec, scaleX, scaleY, scaleEase)

def mnu_rotate(CID, isNewAct, rotateSec, rotate, rotateEase):
    chara_act_manual(CID, isNewAct, 0, 0, 0, 0, 0, 0, 0, 0, rotateSec, rotate, rotateEase)

def mnu_fade(CID, isNewAct, fadeSec, fade, fadeEase):
    chara_act_manual(CID, isNewAct, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, fadeSec, fade, fadeEase)

def cmp(CID, sec, moveX, moveY, scaleX, scaleY, rotate, fade):
    chara_act_complete(CID, sec, moveX, moveY, scaleX, scaleY, rotate, fade)

def cmp_move(CID, sec, moveX, moveY):
    chara_act_complete(CID, sec, moveX, moveY)

def cmp_scale(CID, sec, scaleX, scaleY):
    chara_act_complete(CID, sec, -1.0, -1.0, scaleX, scaleY)

def cmp_rotate(CID, sec, rotate):
    chara_act_complete(CID, sec, -1.0, -1.0, -1.0, -1.0, rotate)

def cmp_fade(CID, sec, fade):
    chara_act_complete(CID, sec, -1.0, -1.0, -1.0, -1.0, -1.0, fade)

def c_push_t(CID):
    mnu_move(CID, true, 0.2, 0, 50, EaseOutCubic)
    cmp_move(CID, 0.2, 0, 50)

def c_push_t_slow(CID):
    mnu_move(CID, true, 0.4, 0, 50, EaseOutCubic)
    cmp_move(CID, 0.4, 0, 50)

def c_push_b(CID):
    mnu_move(CID, true, 0.2, 0, -50, EaseOutCubic)
    cmp_move(CID, 0.2, 0, -50)

def c_push_b_slow(CID):
    mnu_move(CID, true, 0.4, 0, -50, EaseOutCubic)
    cmp_move(CID, 0.4, 0, -50)

def c_push_l(CID):
    mnu_move(CID, true, 0.2, -50, 0, EaseOutCubic)
    cmp_move(CID, 0.2, -50, 0)

def c_push2_l(CID):
    mnu_move(CID, true, 0.3, -50, 0, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, 0, EaseOutCubic)
    mnu_move(CID, false, 0.2, -30, 0, EaseOutCubic)
    cmp_move(CID, 1.0, -80, 0)

def c_push2_l_slow(CID):
    mnu_move(CID, true, 0.2, 0, 0, EaseOutCubic)
    mnu_move(CID, false, 0.6, -50, 0, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, 0, EaseOutCubic)
    mnu_move(CID, false, 0.4, -50, 0, EaseOutCubic)
    cmp_move(CID, 1.7, -100, 0)

def c_push3_l(CID):
    mnu_move(CID, true, 0.3, -50, 0, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, 0, EaseOutCubic)
    mnu_move(CID, false, 0.2, -30, 0, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, 0, EaseOutCubic)
    mnu_move(CID, false, 0.1, -15, 0, EaseOutCubic)
    cmp_move(CID, 1.6, -95, 0)

def c_push_r(CID):
    mnu_move(CID, true, 0.2, 50, 0, EaseOutCubic)
    cmp_move(CID, 0.2, 50, 0)

def c_bound_t(CID):
    mnu_move(CID, true, 0.25, 0, 16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -16, EaseOutCubic)
    cmp_move(CID, 0.5, 0, 0)

def c_bound_t_slow(CID):
    mnu_move(CID, true, 0.4, 0, 16, EaseOutCubic)
    mnu_move(CID, false, 0.4, 0, -16, EaseOutCubic)
    cmp_move(CID, 0.8, 0, 0)

def c_bound_b(CID):
    mnu_move(CID, true, 0.25, 0, -16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, 16, EaseOutCubic)
    cmp_move(CID, 0.5, 0, 0)

def c_bound_b_slow(CID):
    mnu_move(CID, true, 0.4, 0, -16, EaseOutCubic)
    mnu_move(CID, false, 0.4, 0, 16, EaseOutCubic)
    cmp_move(CID, 0.8, 0, 0)

def c_bound_b_dr(CID):
    mnu_move(CID, true, 0.7, 0, -16, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, 0, 1)
    mnu_move(CID, false, 0.6, 0, 16, EaseOutCubic)
    cmp_move(CID, 1.5, 0, 0)

def c_bound_l(CID):
    mnu_move(CID, true, 0.25, -16, 0, EaseOutCubic)
    mnu_move(CID, false, 0.25, 16, 0, EaseOutCubic)
    cmp_move(CID, 0.5, 0, 0)

def c_bound_r(CID):
    mnu_move(CID, true, 0.25, 16, 0, EaseOutCubic)
    mnu_move(CID, false, 0.25, -16, 0, EaseOutCubic)
    cmp_move(CID, 0.5, 0, 0)

def c_avoid_l(CID):
    mnu_move(CID, true, 0.3, -200, -50, EaseOutBack)
    cmp_move(CID, 0.3, -200, -50)
    wait(0.3)
    play_sound(SE_046)
    wait(0.1)

def c_avoid_l_return(CID):
    mnu_move(CID, true, 0.3, 200, 50, EaseOutCubic)
    cmp_move(CID, 0.3, 200, 50)

def c_avoid_r(CID):
    mnu_move(CID, true, 0.3, 200, -50, EaseOutBack)
    cmp_move(CID, 0.3, 200, -50)
    wait(0.3)
    play_sound(SE_046)
    wait(0.1)

def c_avoid_r_return(CID):
    mnu_move(CID, true, 0.3, -200, 50, EaseOutCubic)
    cmp_move(CID, 0.3, -200, 50)

def c_bound2_t(CID):
    mnu_move(CID, true, 0.25, 0, 16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, 16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -16, EaseOutCubic)
    cmp_move(CID, 1.0, 0, 0)

def c_bound3_t(CID):
    mnu_move(CID, true, 0.25, 0, 16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, 24, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -24, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, 16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -16, EaseOutCubic)
    cmp_move(CID, 1.5, 0, 0)

def c_bound4_t(CID):
    mnu_move(CID, true, 0.25, 0, 16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, 24, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -24, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, 32, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -32, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, 16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -16, EaseOutCubic)
    cmp_move(CID, 2.0, 0, 0)

def c_bound2_b(CID):
    mnu_move(CID, true, 0.25, 0, -16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, 16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -16, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, 16, EaseOutCubic)
    cmp_move(CID, 1.0, 0, 0)

def c_bound2_b_slow(CID):
    mnu_move(CID, true, 0.5, 0, -12, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, 12, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, -12, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, 12, EaseOutCubic)
    cmp_move(CID, 2.0, 0, 0)

def c_bound3_b_slow(CID):
    mnu_move(CID, true, 0.5, 0, -12, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, 12, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, -12, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, 12, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, -12, EaseOutCubic)
    mnu_move(CID, false, 0.5, 0, 12, EaseOutCubic)
    cmp_move(CID, 3.0, 0, 0)

def c_bound2_l(CID):
    mnu_move(CID, true, 0.25, -16, 0, EaseOutCubic)
    mnu_move(CID, false, 0.25, 16, 0, EaseOutCubic)
    mnu_move(CID, false, 0.25, -16, 0, EaseOutCubic)
    mnu_move(CID, false, 0.25, 16, 0, EaseOutCubic)
    cmp_move(CID, 1.0, 0, 0)

def c_bound2_r(CID):
    mnu_move(CID, true, 0.25, 16, 0, EaseOutCubic)
    mnu_move(CID, false, 0.25, -16, 0, EaseOutCubic)
    mnu_move(CID, false, 0.25, 16, 0, EaseOutCubic)
    mnu_move(CID, false, 0.25, -16, 0, EaseOutCubic)
    cmp_move(CID, 1.0, 0, 0)

def c_swing_h(CID):
    mnu_move(CID, true, 0.25, 16, 0, 9)
    mnu_move(CID, false, 0.25, -32, 0, 9)
    mnu_move(CID, false, 0.25, 16, 0, 9)
    cmp_move(CID, 0.75, 0, 0)

def c_swing2_h(CID):
    mnu_move(CID, true, 0.25, 16, 0, 9)
    mnu_move(CID, false, 0.25, -32, 0, 9)
    mnu_move(CID, false, 0.25, 32, 0, 9)
    mnu_move(CID, false, 0.25, -16, 0, 9)
    cmp_move(CID, 1.0, 0, 0)

def c_swing3_h(CID):
    mnu_move(CID, true, 0.25, 16, 0, 9)
    mnu_move(CID, false, 0.25, -32, 0, 9)
    mnu_move(CID, false, 0.25, 32, 0, 9)
    mnu_move(CID, false, 0.25, -32, 0, 9)
    mnu_move(CID, false, 0.25, 32, 0, 9)
    mnu_move(CID, false, 0.25, -16, 0, 9)
    cmp_move(CID, 1.5, 0, 0)

def c_swing_h_slow(CID):
    mnu_move(CID, true, 0.5, 16, 0, 9)
    mnu_move(CID, false, 0.5, -32, 0, 9)
    mnu_move(CID, false, 0.5, 16, 0, 9)
    cmp_move(CID, 1.5, 0, 0)

def c_swing2_h_slow(CID):
    mnu_move(CID, true, 0.5, 16, 0, 9)
    mnu_move(CID, false, 0.5, -32, 0, 9)
    mnu_move(CID, false, 0.5, 32, 0, 9)
    mnu_move(CID, false, 0.5, -16, 0, 9)
    cmp_move(CID, 2.0, 0, 0)

def c_swing3_h_slow(CID):
    mnu_move(CID, true, 0.5, 16, 0, 9)
    mnu_move(CID, false, 0.5, -32, 0, 9)
    mnu_move(CID, false, 0.5, 32, 0, 9)
    mnu_move(CID, false, 0.5, -32, 0, 9)
    mnu_move(CID, false, 0.5, 16, 0, 9)
    cmp_move(CID, 2.5, 0, 0)

def c_swing_h_long(CID):
    mnu_move(CID, true, 0.2, 50, 0, 9)
    mnu_move(CID, false, 0.2, -100, 0, 9)
    mnu_move(CID, false, 0.2, 50, 0, 9)
    cmp_move(CID, 0.6, 0, 0)

def c_swing_h_mid(CID):
    mnu_move(CID, true, 0.08, 6, 0, 9)
    mnu_move(CID, false, 0.1, -12, 0, 9)
    mnu_move(CID, false, 0.08, 6, 0, 9)
    cmp_move(CID, 0.26, 0, 0)

def c_swing_h_fast(CID):
    mnu_move(CID, true, 0.1, 10, 0, 9)
    mnu_move(CID, false, 0.1, -20, 0, 9)
    mnu_move(CID, false, 0.1, 10, 0, 9)
    cmp_move(CID, 0.3, 0, 0)

def c_swing2_h_fast(CID):
    mnu_move(CID, true, 0.08, 10, 0, 9)
    mnu_move(CID, false, 0.08, -20, 0, 9)
    mnu_move(CID, false, 0.08, 20, 0, 9)
    mnu_move(CID, false, 0.08, -20, 0, 9)
    mnu_move(CID, false, 0.08, 10, 0, 9)
    cmp_move(CID, 0.4, 0, 0)

def c_swing2_v_fast(CID):
    mnu_move(CID, true, 0.08, 0, 10, 9)
    mnu_move(CID, false, 0.08, 0, -20, 9)
    mnu_move(CID, false, 0.08, 0, 20, 9)
    mnu_move(CID, false, 0.08, 0, -20, 9)
    mnu_move(CID, false, 0.08, 0, 10, 9)
    cmp_move(CID, 0.4, 0, 0)

def c_fallinto(CID):
    mnu_move(CID, true, 0.4, 0, -25, EaseOutCubic)
    mnu_move(CID, false, 0.1, 0, 0, 1)
    mnu_move(CID, false, 0.5, 16, 0, 9)
    mnu_move(CID, false, 0.5, -32, 0, 9)
    mnu_move(CID, false, 0.5, 16, 0, 9)
    cmp_move(CID, 2.0, 0, -25)

def c_jump(CID):
    mnu_move(CID, true, 0.2, 0, 50, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -60, EaseInCubic)
    mnu_move(CID, false, 0.1, 0, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, 0, -4, EaseInCubic)
    cmp_move(CID, 0.6, 0, 0)

def c_jump2(CID):
    mnu_move(CID, true, 0.2, 0, 50, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -60, EaseInCubic)
    mnu_move(CID, false, 0.2, 0, 60, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -60, EaseInCubic)
    mnu_move(CID, false, 0.1, 0, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, 0, -4, EaseInCubic)
    cmp_move(CID, 1.0, 0, 0)

def c_jump3(CID):
    mnu_move(CID, true, 0.2, 0, 50, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -60, EaseInCubic)
    mnu_move(CID, false, 0.2, 0, 60, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -60, EaseInCubic)
    mnu_move(CID, false, 0.2, 0, 60, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -60, EaseInCubic)
    mnu_move(CID, false, 0.1, 0, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, 0, -4, EaseInCubic)
    cmp_move(CID, 1.4, 0, 0)

def c_jump_em(CID):
    mnu_move(CID, true, 0.2, 0, 100, EaseOutCubic)
    mnu_move(CID, false, 0.25, 0, -110, EaseInCubic)
    mnu_move(CID, false, 0.1, 0, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, 0, -4, EaseInCubic)
    cmp_move(CID, 0.65, 0, 0)

def c_jump2_em(CID):
    mnu_move(CID, true, 0.2, 0, 100, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -110, EaseInCubic)
    mnu_move(CID, false, 0.2, 0, 60, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -60, EaseInCubic)
    mnu_move(CID, false, 0.1, 0, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, 0, -4, EaseInCubic)
    cmp_move(CID, 1.0, 0, 0)

def c_jump_l(CID):
    mnu_move(CID, true, 0.2, -50, 50, EaseOutCubic)
    mnu_move(CID, false, 0.2, -50, -60, EaseInCubic)
    mnu_move(CID, false, 0.1, 0, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, 0, -4, EaseInCubic)
    cmp_move(CID, 0.6, -100, 0)

def c_jump_t(CID):
    mnu_move(CID, true, 0.2, 0, 100, EaseOutCubic)
    mnu_move(CID, false, 0.2, 0, -60, EaseInCubic)
    mnu_move(CID, false, 0.1, 0, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, 0, -4, EaseInCubic)
    cmp_move(CID, 1.0, 0, 50)

def c_jab_r(CID):
    mnu_move(CID, true, 0.15, 80, 0, EaseOutCubic)
    mnu_move(CID, false, 0.1, -80, 0, EaseInCubic)
    cmp_move(CID, 0.25, 0, 0)

def c_jab_l(CID):
    mnu_move(CID, true, 0.15, -80, 0, EaseOutCubic)
    mnu_move(CID, false, 0.1, 80, 0, EaseInCubic)
    cmp_move(CID, 0.25, 0, 0)

def c_shrink_stay(CID):
    mnu_scale(CID, true, 0.2, 0.9, 0.9, EaseOutCubic)
    cmp_scale(CID, 0.2, 0.9, 0.9)

def c_zoom_short(CID):
    mnu_scale(CID, true, 0.15, 1.1, 1.1, EaseOutCubic)
    mnu_scale(CID, false, 0.15, 1, 1, EaseInQuart)
    cmp_scale(CID, 0.3, 1, 1)

def c_zoom(CID):
    mnu_scale(CID, true, 0.2, 1.1, 1.1, EaseOutCubic)
    mnu_scale(CID, false, 0.2, 1, 1, EaseInQuart)
    cmp_scale(CID, 0.4, 1, 1)

def c_zoom_wide(CID):
    mnu_scale(CID, true, 0.2, 1.3, 1.3, EaseOutCubic)
    mnu_scale(CID, false, 0.2, 1, 1, EaseInQuart)
    cmp_scale(CID, 0.4, 1, 1)

def c_zoom2_wide(CID):
    mnu_scale(CID, true, 0.2, 1.3, 1.3, EaseOutCubic)
    mnu_scale(CID, false, 0.2, 1, 1, EaseInQuart)
    mnu_scale(CID, false, 0.2, 1.3, 1.3, EaseOutQuart)
    mnu_scale(CID, false, 0.2, 1, 1, EaseInQuart)
    cmp_scale(CID, 0.8, 1, 1)

def c_zoom_stay(CID):
    mnu_scale(CID, true, 0.2, 1.1, 1.1, EaseOutCubic)
    cmp_scale(CID, 0.2, 1.1, 1.1)

def c_zoom_wide_stay(CID):
    mnu_scale(CID, true, 0.2, 1.3, 1.3, EaseOutCubic)
    cmp_scale(CID, 0.2, 1.3, 1.3)

def c_mnu_def(CID):
    mnu(CID, true, 0.1, 0, 0, 1, 0.1, 1, 1, 1, 0.1, 0, 1, 0.1, 1, 1)
    cmp(CID, 0.1, 0, 0, 1, 1, 0, 1)

def c_mnu_reset(CID):
    mnu(CID, true, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1)
    cmp(CID, 0, 0, 0, 1, 1, 0, 0)

def c_zigzag_h_b(CID):
    mnu_move(CID, true, 0.5, 16, -15, 9)
    mnu_move(CID, false, 0.5, -32, -15, 9)
    mnu_move(CID, false, 0.5, 16, -20, 9)
    cmp_move(CID, 1.5, 0, -50)

def c_zigzag_h_t(CID):
    mnu_move(CID, true, 0.5, 16, 15, 9)
    mnu_move(CID, false, 0.5, -32, 15, 9)
    mnu_move(CID, false, 0.5, 16, 20, 9)
    cmp_move(CID, 1.5, 0, 50)

def c_zigzag_v_r(CID):
    mnu_move(CID, true, 0.5, 15, 16, 9)
    mnu_move(CID, false, 0.5, 15, -32, 9)
    mnu_move(CID, false, 0.5, 20, 16, 9)
    cmp_move(CID, 1.5, 50, 0)

def c_zigzag_v_l(CID):
    mnu_move(CID, true, 0.5, -15, 16, 9)
    mnu_move(CID, false, 0.5, -15, -32, 9)
    mnu_move(CID, false, 0.5, -20, 16, 9)
    cmp_move(CID, 1.5, -50, 0)

def c_kurukuru2(CID):
    mnu_move(CID, true, 0.065, -10, 4.1, 1)
    mnu_move(CID, false, 0.065, -4.1, 10, 1)
    mnu_move(CID, false, 0.065, 4.1, 10, 1)
    mnu_move(CID, false, 0.065, 10, 4.1, 1)
    mnu_move(CID, false, 0.065, 10, -4.1, 1)
    mnu_move(CID, false, 0.065, 4.1, -10, 1)
    mnu_move(CID, false, 0.065, -4.1, -10, 1)
    mnu_move(CID, false, 0.065, -10, -4.1, 1)
    mnu_move(CID, false, 0.065, -10, 4.1, 1)
    mnu_move(CID, false, 0.065, -4.1, 10, 1)
    mnu_move(CID, false, 0.065, 4.1, 10, 1)
    mnu_move(CID, false, 0.065, 10, 4.1, 1)
    mnu_move(CID, false, 0.065, 10, -4.1, 1)
    mnu_move(CID, false, 0.065, 4.1, -10, 1)
    mnu_move(CID, false, 0.065, -4.1, -10, 1)
    mnu_move(CID, false, 0.065, -10, -4.1, 1)
    cmp_move(CID, 1.04, 0, 0)
    wait(0.0)

def c_falldown_r(CID, X, Y, SE):
    mnu_move(CID, true, 0.2, 40, 50, EaseOutCubic)
    mnu(CID, false, 0.2, 40, -260, EaseInCubic, 0.2, 1, 1, 1, 0.2, -30, 1, 0.2, 1, 1)
    mnu_move(CID, false, 0.1, 20, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, 20, -4, EaseInCubic)
    cmp(CID, 0.6, 120, -200, 1, 1, -30, 1)
    wait(0.3)
    play_sound(SE_065)
    wait(0.1)
    StopEye_close(CID)
    set_BG_effect(EFF_001)
    set_BG_effect_pos(EFF_001, X, Y)
    wait(0.05)
    play_sound(SE)
    effect_shake_bg(12, 0.2, 1.0)

def c_falldown_l(CID, X, Y, SE):
    mnu_move(CID, true, 0.2, -40, 50, EaseOutCubic)
    mnu(CID, false, 0.2, -40, -260, EaseInCubic, 0.2, 1, 1, 1, 0.2, 30, 1, 0.2, 1, 1)
    mnu_move(CID, false, 0.1, -20, 14, EaseOutCubic)
    mnu_move(CID, false, 0.1, -20, -4, EaseInCubic)
    cmp(CID, 0.6, -120, -200, 1, 1, -30, 1)
    wait(0.3)
    play_sound(SE_065)
    wait(0.1)
    StopEye_close(CID)
    set_BG_effect(EFF_001)
    set_BG_effect_pos(EFF_001, X, Y)
    wait(0.05)
    play_sound(SE)
    effect_shake_bg(12, 0.2, 1.0)

def Reset(SEC, CAMERA):
    blur(false, SEC, 1.0, 1.0, CAMERA)
    bloom(CAMERA, SEC)
    color_adjustment(CAMERA, SEC)
    post_film(CAMERA, SEC, -1, -1)

def ResetLerp(SEC, CAMERA):
    blur(false, SEC, 1.0, 1.0, CAMERA)
    bloom(CAMERA, SEC)
    color_adjustment(CAMERA, SEC)
    post_film(CAMERA, SEC, filmMode_Lerp, -1, 0.0)

def Sepia(SEC, CAMERA):
    bloom(CAMERA, SEC, -1, 0.8, -1, -1)
    color_adjustment(CAMERA, SEC, 1.0, 0.0, 1.0)
    post_film(CAMERA, SEC, filmMode_Mul, 1.0, 1.57, 118, 96, 80, 1.0)

def Negaposi(SEC, CAMERA, R, G, B):
    bloom(CAMERA, SEC, -1, 0.0, -1, -1)
    color_adjustment(CAMERA, SEC, 1.0, 1.0, 1.0)
    post_film(CAMERA, SEC, filmMode_Lerp, 0.0, 1.57, R, G, B, 1.0)

def SEPIA_SCREEN():
    Sepia(0, 2)

def NEGA_SCREEN():
    Negaposi(0.5, 1, 124, 88, 176)

def RESET_SCREEN():
    Reset(0, 0)
    ResetLerp(0, 0)
    Reset(0, 1)
    ResetLerp(0, 1)
    Reset(0, 2)
    ResetLerp(0, 2)

def SCREEN_COLOR_DEF():
    fade_color(1.0, 0, 0, 0, 0)

def BLACK_SCREEN():
    WFOUT_SHORT()
    fade_color(1.0, 0, 0, 0, 0.7)

def StopEye(CID):
    chara_eyeblink(CID, -1)

def StopEye_close(CID):
    chara_eyeblink(CID, -2)

def RestartEye(CID):
    chara_eyeblink(CID)

def StopLip(CID):
    chara_lipsynch(CID, -2)

def StopLip_close(CID):
    chara_lipsynch(CID, -1)

def RestartLip(CID):
    chara_lipsynch(CID)

def WAIT_LIP(CID, sec):
    StopLip_close(CID)
    wait(sec)
    RestartLip(CID)

def RestartAll(CID):
    RestartEye(CID)
    RestartLip(CID)

def SHAKE_BG_LOOP(SHAKE_VALUE, PEEC_SEC):
    effect_shake_bg(SHAKE_VALUE, PEEC_SEC, -1)

def SHAKE_BG_STOP(SHAKE_VALUE, STOP_SEC):
    effect_shake_bg(SHAKE_VALUE, -1, STOP_SEC)

def SHAKE_CH_LOOP(SHAKE_VALUE, PEEC_SEC):
    effect_shake_chara(SHAKE_VALUE, PEEC_SEC, -1)

def SHAKE_CH_STOP(SHAKE_VALUE, STOP_SEC):
    effect_shake_chara(SHAKE_VALUE, -1, STOP_SEC)

def TUTORIAL_BUTTON_SETTING():
    button_visible(false, 0, false)

def OL_CENTER():
    outline_centering(true)

def OL_LEFT():
    outline_centering(false)

def OL_TITLE(title):
    outline_title(title)

def DRAGON_TALK_STOP():
    dragon_talk(false)

def RESET_TEXT():
    reset_text()

def CHARA_INTRO(CID, NAME, ANOTHER, ANOTHER_RUBY, AFFLIATION, AFFLIATION_RUBY, EMBLEM_NAME):
    chara_intro(CID, NAME, ANOTHER, ANOTHER_RUBY, AFFLIATION, AFFLIATION_RUBY, EMBLEM_NAME)

def REMOVE_CHARA_INTRO():
    chara_intro(0)

def CHARA_INTRO_SET(CID, NAME, ANOTHER, ANOTHER_RUBY, AFFLIATION, AFFLIATION_RUBY, EMBLEM_NAME):
    button_visible(false, 0.3, false)
    post_film(0, 0.5, filmMode_Mul, 0.5, 0, 0, 0, 0, 1.0)
    wait(0.5)
    if(EMBLEM_NAME == Icon_Emblem_Story_01):
        play_sound(SE_207)
    elif(EMBLEM_NAME == Icon_Emblem_Story_02):
        play_sound(SE_266)
    elif(EMBLEM_NAME == Icon_Emblem_Story_03):
        play_sound(SE_207)
    else:
        play_sound(SE_207)
    frame_visible(false, 0)
    CHARA_INTRO(CID, NAME, ANOTHER, ANOTHER_RUBY, AFFLIATION, AFFLIATION_RUBY, EMBLEM_NAME)
    wait(0.6)
    if(EMBLEM_NAME == Icon_Emblem_Story_01):
        set_BG_effect(EFF_SCE_2D_CMN_110)
    elif(EMBLEM_NAME == Icon_Emblem_Story_03):
        set_BG_effect(EFF_SCE_2D_CMN_110)
    wait(1.7)
    touch_wait()
    NO_EFFECT()
    chara_intro_end()
    wait(1.0)
    REMOVE_CHARA_INTRO()
    frame_visible(true, 0)
    Reset(0.5, 0)
    wait(0.5)
    button_visible(false, 0, true)

def CHARA_INTRO_SET_EFF(CID, NAME, ANOTHER, ANOTHER_RUBY, AFFLIATION, AFFLIATION_RUBY, EMBLEM_NAME, EFF, EFF2, trigger, trigger2):
    screen_fadeout(0.5, 0, 0, 0)
    NO_EFFECT()
    button_visible(false, 0.3, false)
    post_film(0, 0, filmMode_Mul, 0.5, 0, 0, 0, 0, 1.0)
    screen_fadein(0, 0, 0, 0)
    if(EMBLEM_NAME == Icon_Emblem_Story_01):
        play_sound(SE_207)
    elif(EMBLEM_NAME == Icon_Emblem_Story_02):
        play_sound(SE_266)
    elif(EMBLEM_NAME == Icon_Emblem_Story_03):
        play_sound(SE_207)
    else:
        play_sound(SE_207)
    frame_visible(false, 0)
    CHARA_INTRO(CID, NAME, ANOTHER, ANOTHER_RUBY, AFFLIATION, AFFLIATION_RUBY, EMBLEM_NAME)
    wait(0.7)
    if(EMBLEM_NAME == Icon_Emblem_Story_01):
        set_BG_effect(EFF_SCE_2D_CMN_110)
    elif(EMBLEM_NAME == Icon_Emblem_Story_03):
        set_BG_effect(EFF_SCE_2D_CMN_110)
    wait(1.7)
    touch_wait()
    NO_EFFECT()
    chara_intro_end()
    wait(1.0)
    REMOVE_CHARA_INTRO()
    frame_visible(true, 0)
    screen_fadeout(0, 0, 0, 0)
    Reset(0, 0)
    set_BG_effect(EFF, EFF2)
    set_BG_effect_trigger(trigger, trigger2)
    screen_fadein(0.5, 0, 0, 0)
    button_visible(false, 0, true)

def CHARA_INTRO_SET_DARK(CID, NAME, ANOTHER, ANOTHER_RUBY, AFFLIATION, AFFLIATION_RUBY, EMBLEM_NAME):
    button_visible(false, 0.3, false)
    post_film(0, 0.5, filmMode_Mul, 0.5, 0, 0, 0, 0, 1.0)
    wait(0.5)
    if(EMBLEM_NAME == Icon_Emblem_Story_01):
        play_sound(SE_207)
    elif(EMBLEM_NAME == Icon_Emblem_Story_02):
        play_sound(SE_266)
    elif(EMBLEM_NAME == Icon_Emblem_Story_03):
        play_sound(SE_207)
    else:
        play_sound(SE_207)
    frame_visible(false, 0)
    CHARA_INTRO(CID, NAME, ANOTHER, ANOTHER_RUBY, AFFLIATION, AFFLIATION_RUBY, EMBLEM_NAME)
    wait(0.6)
    if(EMBLEM_NAME == Icon_Emblem_Story_01):
        set_BG_effect(EFF_SCE_2D_CMN_110)
    elif(EMBLEM_NAME == Icon_Emblem_Story_03):
        set_BG_effect(EFF_SCE_2D_CMN_110)
    wait(1.7)
    touch_wait()
    NO_EFFECT()
    chara_intro_end()
    wait(1.0)
    REMOVE_CHARA_INTRO()
    fade_color(0.5, 0, 0, 0, 0.7)
    frame_visible(true, 0)
    Reset(0.5, 0)
    wait(0.5)
    button_visible(false, 0, true)

def CHAPTER_INTRO_START():
    frame_visible(false)
    message_pos(1)
    window_enable(false)
    set_BG(0)

def CHAPTER_INTRO_BAND(LABEL):
    chapter_intro(LABEL)
    chapter_intro_frame_visible(true, 0.7)

def CHAPTER_INTRO_NEXT(LABEL):
    chapter_intro_next(LABEL)

def CHAPTER_INTRO_END():
    message_pos(0)
    frame_visible(true)
    window_enable(true)
    chapter_intro(0)
    chapter_intro_frame_visible(false)

def CHAPTER_INTRO_TEXT():
    text_size(24)
    text_color(255, 255, 255)

def TUTORIAL_START(CID):
    TUTORIAL_BUTTON_SETTING()
    window_type(NORMAL)
    fade_color(0.3, 0, 0, 0, 0.5, EaseOutCubic)
    chara_visible(CID, false)
    mnu_fade(CID, true, 0.15, 0.5, 1)
    mnu_fade(CID, false, 0.15, 1.0, 1)
    wait(0.15)
    frame_visible(true, 0.3)
    window_fadein(0, true)
    wait(0.3)
    chara_visible(CID, true)

def CHARA_FROM_ANOTHER_WORLD(eye, lip, X, Y, CID, Face, MinScale, MaxScale, Type, Aura):
    c_mnu_reset(CID)
    touch_enable(false)
    if(Type == Enemy):
        play_sound(SE_011)
        set_BG_effect(EFF_SCE_2D_CMN_046)
        wait(0.5)
    else:
        CHARA_SET_POS_0(eye, lip, X, Y, CID, Face)
        mnu_scale(CID, true, 0.01, MinScale, MinScale, 1)
        cmp_scale(CID, 0.01, MinScale, MinScale)
        play_sound(SE_057)
    if(Type == Enemy):
        set_BG_effect(1, EFF_SCE_2D_CMN_004)
    elif(Type == Chara):
        set_BG_effect(EFF_SCE_2D_CMN_004)
    set_BG_effect_opacity(EFF_SCE_2D_CMN_004, 1)
    set_BG_effect_scale(EFF_SCE_2D_CMN_004, 1, 1)
    set_BG_effect_pos(EFF_SCE_2D_CMN_004, 0, 100)
    if(Type == Enemy):
        set_BG_effect_trigger(0, 8)
    elif(Type == Chara):
        set_BG_effect_trigger(8)
    wait(1.4)
    if(Type == Chara):
        mnu(CID, true, 0.8, 0, 0, EaseInSine, 0.8, MaxScale, MaxScale, EaseInSine, 0.8, 0, EaseInSine, 0.4, 1, EaseInSine)
        cmp(CID, 0.8, 0, 0, MaxScale, MaxScale, 0, 1)
        set_BG_effect_opacity(EFF_SCE_2D_CMN_004, 0, 1.6, 1)
        wait(0.8)
        set_BG_effect_scale(EFF_SCE_2D_CMN_004, 0.01, 0.01, 0.8, 1)
        wait(0.8)
        set_BG_effect(0, 1, 1, 1)
    elif(Type == Enemy):
        mnu(CID, true, 0.8, 0, 0, EaseInSine, 0.8, MaxScale, MaxScale, EaseInSine, 0.8, 0, EaseInSine, 0.4, 1, EaseInSine)
        cmp(CID, 0.8, 0, 0, MaxScale, MaxScale, 0, 1)
    else:
        if(Aura == 1):
            set_BG_effect(1, 1, EFF_SCE_2D_CMN_010, EFF_SCE_2D_CMN_011)
            set_BG_effect_scale(EFF_SCE_2D_CMN_010, MaxScale, MaxScale)
            set_BG_effect_scale(EFF_SCE_2D_CMN_011, MaxScale, MaxScale)
            set_BG_effect_pos(EFF_SCE_2D_CMN_010, X, Y)
            set_BG_effect_pos(EFF_SCE_2D_CMN_011, X, Y)
            set_BG_effect_trigger(0, 0, 8, 8)
    chara_visible(CID, true)
    touch_enable(true)

def event_still_set(Rayer, Sec, Rayer1, X1, Rayer2, X2, Rayer3, X3):
    if(Rayer == 1):
        CHARA_SET_POS_0(M, M, X1, 0, Rayer1, 1)
        CHARA_UNCOLOR(Rayer1)
        mnu_fade(Rayer1, true, Sec, 1, EaseOutSine)
        cmp_fade(Rayer1, Sec, 1)
    elif(Rayer == 2):
        CHARA_SET_POS_0(M, M, X1, 0, Rayer1, 1)
        CHARA_SET_POS_0(M, M, X2, 0, Rayer2, 1)
        CHARA_UNCOLOR(Rayer1)
        CHARA_UNCOLOR(Rayer2)
        mnu_fade(Rayer1, true, Sec, 1, EaseOutSine)
        mnu_fade(Rayer2, true, Sec, 1, EaseOutSine)
        cmp_fade(Rayer1, Sec, 1)
        cmp_fade(Rayer2, Sec, 1)
    elif(Rayer == 3):
        CHARA_SET_POS_0(M, M, X1, 0, Rayer1, 1)
        CHARA_SET_POS_0(M, M, X2, 0, Rayer2, 1)
        CHARA_SET_POS_0(M, M, X3, 0, Rayer3, 1)
        CHARA_UNCOLOR(Rayer1)
        CHARA_UNCOLOR(Rayer2)
        CHARA_UNCOLOR(Rayer3)
        mnu_fade(Rayer1, true, Sec, 1, EaseOutSine)
        mnu_fade(Rayer2, true, Sec, 1, EaseOutSine)
        mnu_fade(Rayer3, true, Sec, 1, EaseOutSine)
        cmp_fade(Rayer1, Sec, 1)
        cmp_fade(Rayer2, Sec, 1)
        cmp_fade(Rayer3, Sec, 1)
    else:
        pass

def event_still_move(Rayer, Sec, Rayer1, move1, Rayer2, move2, Rayer3, move3):
    if(Rayer == 1):
        mnu_move(Rayer1, true, Sec, move1, 0, 1)
        cmp_move(Rayer1, Sec, move1, 0)
    elif(Rayer == 2):
        mnu_move(Rayer1, true, Sec, move1, 0, 1)
        mnu_move(Rayer2, true, Sec, move2, 0, 1)
        cmp_move(Rayer1, Sec, move1, 0)
        cmp_move(Rayer2, Sec, move2, 0)
    elif(Rayer == 3):
        mnu_move(Rayer1, true, Sec, move1, 0, 1)
        mnu_move(Rayer2, true, Sec, move2, 0, 1)
        mnu_move(Rayer3, true, Sec, move3, 0, 1)
        cmp_move(Rayer1, Sec, move1, 0)
        cmp_move(Rayer2, Sec, move2, 0)
        cmp_move(Rayer3, Sec, move3, 0)
    else:
        pass

def MONSTER_SET3_FRONT(IN, CID, CID2, CID3):
    chara_visible(CID, false)
    chara_visible(CID2, false)
    chara_visible(CID3, false)
    chara_pos(CID, 200, 0)
    chara_pos(CID2, -200, 0)
    chara_pos(CID3, 0, 50)
    chara_face(CID, 12)
    chara_face(CID2, 12)
    chara_face(CID3, 12)
    mnu_scale(CID3, true, 0.01, 1.0, 1.0, EaseOutCubic)
    mnu_scale(CID2, true, 0.01, 0.7, 0.7, EaseOutCubic)
    mnu_scale(CID, true, 0.01, 0.7, 0.7, EaseOutCubic)
    cmp_scale(CID3, 0.01, 1.0, 1.0)
    cmp_scale(CID2, 0.01, 0.7, 0.7)
    cmp_scale(CID, 0.01, 0.7, 0.7)
    wait(0.01)
    if(IN == KAMITE):
        KAMITE_IN_DEF(CID)
        KAMITE_IN_DEF(CID2)
        wait(0.2)
        mnu(CID3, true, 0.05, 120, 0, 1, 0.05, 1, 1, 1, 0.05, 0, 1, 0.05, 0, 1)
        mnu(CID3, false, 0.4, -120, 0, EaseOutSine, 0.4, 1, 1, 1, 0.4, 0, 1, 0.4, 1, EaseOutSine)
        cmp(CID3, 0.45, 0, 0, 1, 1, 0, 1)
        NO_EMO(CID)
        NO_EMO(CID2)
        wait(0.45)
    elif(IN == SHIMOTE):
        SHIMOTE_IN_DEF(CID)
        SHIMOTE_IN_DEF(CID2)
        wait(0.2)
        mnu(CID3, true, 0.05, -120, 0, 1, 0.05, 1, 1, 1, 0.05, 0, 1, 0.05, 0, 1)
        mnu(CID3, false, 0.4, 120, 0, EaseOutSine, 0.4, 1, 1, 1, 0.4, 0, 1, 0.4, 1, EaseOutSine)
        cmp(CID3, 0.45, 0, 0, 1, 1, 0, 1)
        NO_EMO(CID)
        NO_EMO(CID2)
        wait(0.45)
    else:
        mnu_fade(CID3, true, 0.4, 1.0, 1)
        mnu_fade(CID, true, 0.4, 1.0, 1)
        mnu_fade(CID2, true, 0.4, 1.0, 1)
        cmp_fade(CID3, 0.4, 1.0)
        cmp_fade(CID, 0.4, 1.0)
        cmp_fade(CID2, 0.4, 1.0)
        wait(0.4)

def Pull_in(eye1, lip1, CID, int, eye2, lip2, CID2, int2, front):
    c_face(eye1, lip1, CID, int)
    mnu_move(CID, true, 0.3, 120, 0, EaseOutSine)
    cmp_move(CID, 0.3, 120, 0)
    wait(0.3)
    CHARA_SET_0(eye2, lip2, R, CID2, int2)
    chara_pos(CID2, 360, 0)
    play_sound(SE_047)
    if(front == 1):
        mnu_move(CID, true, 0.3, -90, 0, EaseOutSine)
        mnu(CID2, true, 0.3, -90, 0, EaseOutSine, 0.3, 1.0, 1.0, EaseOutSine, 0.3, 0, EaseOutSine, 0.3, 1, EaseOutSine)
        cmp_move(CID, 0.3, -90, 0)
        cmp(CID2, 0.3, -90, 0, 1, 1, 0, 1)
        wait(0.7)
        play_sound(SE_047)
        mnu_move(CID, true, 0.3, -90, 0, EaseOutSine)
        mnu_move(CID2, true, 0.3, -90, 0, EaseOutSine)
        cmp_move(CID, 0.3, -90, 0)
        cmp_move(CID2, 0.3, -90, 0)
    else:
        mnu(CID2, true, 0.3, -90, 0, EaseOutSine, 0.3, 1.0, 1.0, EaseOutSine, 0.3, 0, EaseOutSine, 0.3, 1, EaseOutSine)
        mnu_move(CID, true, 0.3, -90, 0, EaseOutSine)
        cmp(CID2, 0.3, -90, 0, 1, 1, 0, 1)
        cmp_move(CID, 0.3, -90, 0)
        wait(0.7)
        play_sound(SE_047)
        mnu_move(CID2, true, 0.3, -90, 0, EaseOutSine)
        mnu_move(CID, true, 0.3, -90, 0, EaseOutSine)
        cmp_move(CID2, 0.3, -90, 0)
        cmp_move(CID, 0.3, -90, 0)
    wait(0.7)

def CHARA_BEAT_MALIONE(CID, X, Y, R):
    set_BG_effect(EFF_SCE_2D_CMN_145)
    set_BG_effect_pos(EFF_SCE_2D_CMN_145, X, Y)
    set_BG_effect_scale(EFF_SCE_2D_CMN_145, 1.3, 0.25)
    set_BG_effect_color(EFF_SCE_2D_CMN_145, 255, 198, 107)
    set_BG_effect_rotation(EFF_SCE_2D_CMN_145, R)
    set_BG_effect_speed(EFF_SCE_2D_CMN_145, 1)
    play_sound(SE_STORY_COMMON_0012)
    play_sound(SE_STORY_COMMON_0234)
    c_swing2_h_fast(CID)
    wait(0.25)

def CHARA_BEAT_MALIONE2(CID):
    set_BG_effect(EFF_SCE_2D_CMN_145)
    set_BG_effect_pos(EFF_SCE_2D_CMN_145, 100, 60)
    set_BG_effect_scale(EFF_SCE_2D_CMN_145, 1.3, 0.25)
    set_BG_effect_color(EFF_SCE_2D_CMN_145, 255, 198, 107)
    set_BG_effect_rotation(EFF_SCE_2D_CMN_145, 190)
    set_BG_effect_speed(EFF_SCE_2D_CMN_145, 1.5)
    play_sound(SE_STORY_COMMON_0012)
    play_sound(SE_STORY_COMMON_0234)
    c_swing2_h_fast(CID)
    wait(0.25)
    set_BG_effect(1, EFF_SCE_2D_CMN_145)
    set_BG_effect_pos(EFF_SCE_2D_CMN_145, -100, 60)
    set_BG_effect_scale(EFF_SCE_2D_CMN_145, 1.3, 0.25)
    set_BG_effect_color(EFF_SCE_2D_CMN_145, 255, 198, 107)
    set_BG_effect_rotation(EFF_SCE_2D_CMN_145, 340)
    set_BG_effect_speed(EFF_SCE_2D_CMN_145, 1.5)
    play_sound(SE_STORY_COMMON_0012)
    play_sound(SE_STORY_COMMON_0234)
    wait(0.25)

def CHARA_GUARD_MALIONE2(CID):
    SCREEN_FLASH_WHITE_DEF()
    set_BG_effect(EFF_SCE_2D_CMN_145, 0, EFF_SCE_2D_CMN_089)
    set_BG_effect_pos(EFF_SCE_2D_CMN_145, -150, 145)
    set_BG_effect_scale(EFF_SCE_2D_CMN_145, 1.3, 0.25)
    set_BG_effect_color(EFF_SCE_2D_CMN_145, 255, 198, 107)
    set_BG_effect_rotation(EFF_SCE_2D_CMN_145, -35)
    set_BG_effect_speed(EFF_SCE_2D_CMN_145, 1.5)
    play_sound(SE_STORY_COMMON_0013)
    c_swing2_h_fast(CID)
    wait(0.3)
    set_BG_effect(1, EFF_SCE_2D_CMN_145, 1)
    set_BG_effect_pos(EFF_SCE_2D_CMN_145, 150, 180)
    set_BG_effect_scale(EFF_SCE_2D_CMN_145, 1.3, 0.25)
    set_BG_effect_color(EFF_SCE_2D_CMN_145, 255, 198, 107)
    set_BG_effect_rotation(EFF_SCE_2D_CMN_145, 210)
    set_BG_effect_speed(EFF_SCE_2D_CMN_145, 1.5)
    play_sound(SE_STORY_COMMON_0013)
    wait(0.25)

def eyeblink(CID, eye):
    if(eye == O):
        chara_eyeblink(CID, -1)
    elif(eye == Q):
        chara_eyeblink(CID, -2)
    elif(eye == M):
        chara_eyeblink(CID)
    else:
        chara_eyeblink(CID)

def lipsynch(CID, lip):
    if(lip == O):
        chara_lipsynch(CID, -2)
    elif(lip == Q):
        chara_lipsynch(CID, -1)
    elif(lip == M):
        chara_lipsynch(CID)
    else:
        chara_lipsynch(CID)

def _CharaSet(style, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3):
    if(style == KAMITE):
        chara_visible(CID, false)
        chara_pos(CID, posX, posY)
        chara_act_manual(CID, true, 0.01, 120, 0, 1)
        chara_act_complete(CID, 0.01, 120, 0)
        wait(0.01)
        if(posY == C):
            chara_act_manual(CID, true, 0.01, 0, -2, 1)
            chara_act_complete(CID, 0.01, 0, -2)
        wait(0.01)
        chara_face(CID, face)
        eyeblink(CID, eye)
        lipsynch(CID, lip)
        if(CID2 == 0):
            pass
        else:
            chara_visible(CID2, false)
            chara_pos(CID2, posX2, posY2)
            chara_act_manual(CID2, true, 0.01, 120, 0, 1)
            chara_act_complete(CID2, 0.01, 120, 0)
            wait(0.01)
            if(posY2 == C):
                chara_act_manual(CID2, true, 0.01, 0, -2, 1)
                chara_act_complete(CID2, 0.01, 0, -2)
            wait(0.01)
            chara_face(CID2, face2)
            eyeblink(CID2, eye2)
            lipsynch(CID2, lip2)
        if(CID3 == 0):
            pass
        else:
            chara_visible(CID3, false)
            chara_pos(CID3, posX3, posY3)
            chara_act_manual(CID3, true, 0.01, 120, 0, 1)
            chara_act_complete(CID3, 0.01, 120, 0)
            wait(0.01)
            if(posY3 == C):
                chara_act_manual(CID3, true, 0.01, 0, -2, 1)
                chara_act_complete(CID3, 0, 0.01, -2)
            wait(0.01)
            chara_face(CID3, face3)
            eyeblink(CID3, eye3)
            lipsynch(CID3, lip3)
    elif(style == SHIMOTE):
        chara_visible(CID, false)
        chara_pos(CID, posX, posY)
        chara_act_manual(CID, true, 0.01, -120, 0, 1)
        chara_act_complete(CID, 0.01, -120, 0)
        wait(0.01)
        if(posY == C):
            chara_act_manual(CID, true, 0.01, 0, -2, 1)
            chara_act_complete(CID, 0.01, 0, -2)
        wait(0.01)
        chara_face(CID, face)
        eyeblink(CID, eye)
        lipsynch(CID, lip)
        if(CID2 == 0):
            pass
        else:
            chara_visible(CID2, false)
            chara_pos(CID2, posX2, posY2)
            chara_act_manual(CID2, true, 0.01, -120, 0, 1)
            chara_act_complete(CID2, 0.01, -120, 0)
            wait(0.01)
            if(posY2 == C):
                chara_act_manual(CID2, true, 0.01, 0, -2, 1)
                chara_act_complete(CID2, 0.01, 0, -2)
            wait(0.01)
            chara_face(CID2, face2)
            eyeblink(CID2, eye2)
            lipsynch(CID2, lip2)
        if(CID3 == 0):
            pass
        else:
            chara_visible(CID3, false)
            chara_pos(CID3, posX3, posY3)
            chara_act_manual(CID3, true, 0.01, -120, 0, 1)
            chara_act_complete(CID3, 0.01, -120, 0)
            wait(0.01)
            if(posY3 == C):
                chara_act_manual(CID3, true, 0.01, 0, -2, 1)
                chara_act_complete(CID3, 0.01, 0, -2)
            wait(0.01)
            chara_face(CID3, face3)
            eyeblink(CID3, eye3)
            lipsynch(CID3, lip3)
    elif(style == TOP):
        chara_visible(CID, false)
        chara_pos(CID, posX, posY)
        chara_act_manual(CID, true, 0.01, 0, 120, 1)
        chara_act_complete(CID, 0.01, 0, 120)
        wait(0.01)
        if(posY == C):
            chara_act_manual(CID, true, 0.01, 0, -2, 1)
            chara_act_complete(CID, 0.01, 0, -2)
        wait(0.01)
        chara_face(CID, face)
        eyeblink(CID, eye)
        lipsynch(CID, lip)
        if(CID2 == 0):
            pass
        else:
            chara_visible(CID2, false)
            chara_pos(CID2, posX2, posY2)
            chara_act_manual(CID2, true, 0.01, 0, 120, 1)
            chara_act_complete(CID2, 0.01, 0, 120)
            wait(0.01)
            if(posY2 == C):
                chara_act_manual(CID2, true, 0.01, 0, -2, 1)
                chara_act_complete(CID2, 0.01, 0, -2)
            wait(0.01)
            chara_face(CID2, face2)
            eyeblink(CID2, eye2)
            lipsynch(CID2, lip2)
        if(CID3 == 0):
            pass
        else:
            chara_visible(CID3, false)
            chara_pos(CID3, posX3, posY3)
            chara_act_manual(CID3, true, 0.01, 0, 120, 1)
            chara_act_complete(CID3, 0.01, 0, 120)
            wait(0.01)
            if(posY3 == C):
                chara_act_manual(CID3, true, 0.01, 0, -2, 1)
                chara_act_complete(CID3, 0.01, 0, -2)
            wait(0.01)
            chara_face(CID3, face3)
            eyeblink(CID3, eye3)
            lipsynch(CID3, lip3)
    elif(style == BOTTOM):
        chara_visible(CID, false)
        chara_pos(CID, posX, posY)
        chara_act_manual(CID, true, 0.01, 0, -120, 1)
        chara_act_complete(CID, 0.01, 0, -120)
        wait(0.01)
        if(posY == C):
            chara_act_manual(CID, true, 0.01, 0, -2, 1)
            chara_act_complete(CID, 0.01, 0, -2)
        wait(0.01)
        chara_face(CID, face)
        eyeblink(CID, eye)
        lipsynch(CID, lip)
        if(CID2 == 0):
            pass
        else:
            chara_visible(CID2, false)
            chara_pos(CID2, posX2, posY2)
            chara_act_manual(CID2, true, 0.01, 0, -120, 1)
            chara_act_complete(CID2, 0.01, 0, -120)
            wait(0.01)
            if(posY2 == C):
                chara_act_manual(CID2, true, 0.01, 0, -2, 1)
                chara_act_complete(CID2, 0.01, 0, -2)
            wait(0.01)
            chara_face(CID2, face2)
            eyeblink(CID2, eye2)
            lipsynch(CID2, lip2)
        if(CID3 == 0):
            pass
        else:
            chara_visible(CID3, false)
            chara_pos(CID3, posX3, posY3)
            chara_act_manual(CID3, true, 0.01, 0, -120, 1)
            chara_act_complete(CID3, 0.01, 0, -120)
            wait(0.01)
            if(posY3 == C):
                chara_act_manual(CID3, true, 0.01, 0, -2, 1)
                chara_act_complete(CID3, 0.01, 0, -2)
            wait(0.01)
            chara_face(CID3, face3)
            eyeblink(CID3, eye3)
            lipsynch(CID3, lip3)
    else:
        chara_visible(CID, false)
        chara_pos(CID, posX, posY)
        if(posY == C):
            chara_act_manual(CID, true, 0.01, 0, -2, 1)
            chara_act_complete(CID, 0.01, 0, -2)
        wait(0.01)
        chara_face(CID, face)
        eyeblink(CID, eye)
        lipsynch(CID, lip)
        if(CID2 == 0):
            pass
        else:
            chara_visible(CID2, false)
            chara_pos(CID2, posX2, posY2)
            if(posY2 == C):
                chara_act_manual(CID2, true, 0.01, 0, -2, 1)
                chara_act_complete(CID2, 0.01, 0, -2)
            wait(0.01)
            chara_face(CID2, face2)
            eyeblink(CID2, eye2)
            lipsynch(CID2, lip2)
        if(CID3 == 0):
            pass
        else:
            chara_visible(CID3, false)
            chara_pos(CID3, posX3, posY3)
            if(posY3 == C):
                chara_act_manual(CID3, true, 0.01, 0, -2, 1)
                chara_act_complete(CID3, 0.01, 0, -2)
            wait(0.01)
            chara_face(CID3, face3)
            eyeblink(CID3, eye3)
            lipsynch(CID3, lip3)

def CharaSet(style, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3):
    if(style == KAMITE):
        _CharaSet(KAMITE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, WAIT, -120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE):
        _CharaSet(SHIMOTE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, WAIT, 120, 0, CID, CID2, CID3)
    elif(style == TOP):
        _CharaSet(TOP, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, WAIT, 0, -120, CID, CID2, CID3)
    elif(style == BOTTOM):
        _CharaSet(BOTTOM, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, WAIT, 0, 120, CID, CID2, CID3)
    elif(style == KAMITE_REVERSE):
        _CharaSet(KAMITE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, REVERSE, -120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE_REVERSE):
        _CharaSet(SHIMOTE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, REVERSE, 120, 0, CID, CID2, CID3)
    elif(style == TOP_REVERSE):
        _CharaSet(TOP, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, REVERSE, 0, -120, CID, CID2, CID3)
    elif(style == BOTTOM_REVERSE):
        _CharaSet(BOTTOM, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, REVERSE, 0, 120, CID, CID2, CID3)
    elif(style == KAMITE_SYNC):
        _CharaSet(KAMITE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, SYNC, -120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE_SYNC):
        _CharaSet(SHIMOTE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, SYNC, 120, 0, CID, CID2, CID3)
    elif(style == TOP_SYNC):
        _CharaSet(TOP, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, SYNC, 0, -120, CID, CID2, CID3)
    elif(style == BOTTOM_SYNC):
        _CharaSet(BOTTOM, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, SYNC, 0, 120, CID, CID2, CID3)
    else:
        _CharaSet(style, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.3, SYNC, 0, 0, CID, CID2, CID3)

def CharaDel(style, CID, CID2, CID3):
    if(style == KAMITE):
        CharaOut(0.4, WAIT, 120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE):
        CharaOut(0.4, WAIT, -120, 0, CID, CID2, CID3)
    elif(style == TOP):
        CharaOut(0.4, WAIT, 0, 120, CID, CID2, CID3)
    elif(style == BOTTOM):
        CharaOut(0.4, WAIT, 0, -120, CID, CID2, CID3)
    elif(style == KAMITE_REVERSE):
        CharaOut(0.4, REVERSE, 120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE_REVERSE):
        CharaOut(0.4, REVERSE, -120, 0, CID, CID2, CID3)
    elif(style == TOP_REVERSE):
        CharaOut(0.4, REVERSE, 0, 120, CID, CID2, CID3)
    elif(style == BOTTOM_REVERSE):
        CharaOut(0.4, REVERSE, 0, -120, CID, CID2, CID3)
    elif(style == KAMITE_SYNC):
        CharaOut(0.4, SYNC, 120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE_SYNC):
        CharaOut(0.4, SYNC, -120, 0, CID, CID2, CID3)
    elif(style == TOP_SYNC):
        CharaOut(0.4, SYNC, 0, 120, CID, CID2, CID3)
    elif(style == BOTTOM_SYNC):
        CharaOut(0.4, SYNC, 0, -120, CID, CID2, CID3)
    else:
        CharaOut(0.3, SYNC, 0, 0, CID, CID2, CID3)

def CharaSetSE(style, SE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3):
    play_sound(SE)
    wait(1.0)
    set_volume(0, 0.5, SE)
    if(style == KAMITE):
        _CharaSet(KAMITE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, WAIT, -120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE):
        _CharaSet(SHIMOTE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, WAIT, 120, 0, CID, CID2, CID3)
    elif(style == TOP):
        _CharaSet(TOP, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, WAIT, 0, -120, CID, CID2, CID3)
    elif(style == BOTTOM):
        _CharaSet(BOTTOM, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, WAIT, 0, 120, CID, CID2, CID3)
    elif(style == KAMITE_REVERSE):
        _CharaSet(KAMITE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, REVERSE, -120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE_REVERSE):
        _CharaSet(SHIMOTE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, REVERSE, 120, 0, CID, CID2, CID3)
    elif(style == TOP_REVERSE):
        _CharaSet(TOP, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, REVERSE, 0, -120, CID, CID2, CID3)
    elif(style == BOTTOM_REVERSE):
        _CharaSet(BOTTOM, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, REVERSE, 0, 120, CID, CID2, CID3)
    elif(style == KAMITE_SYNC):
        _CharaSet(KAMITE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, SYNC, -120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE_SYNC):
        _CharaSet(SHIMOTE, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, SYNC, 120, 0, CID, CID2, CID3)
    elif(style == TOP_SYNC):
        _CharaSet(TOP, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, SYNC, 0, -120, CID, CID2, CID3)
    elif(style == BOTTOM_SYNC):
        _CharaSet(BOTTOM, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.4, SYNC, 0, 120, CID, CID2, CID3)
    else:
        _CharaSet(style, CID, face, eye, lip, posX, posY, CID2, face2, eye2, lip2, posX2, posY2, CID3, face3, eye3, lip3, posX3, posY3)
        CharaIn(0.3, SYNC, 0, 0, CID, CID2, CID3)

def CharaDelSE(style, SE, CID, CID2, CID3):
    play_sound(SE)
    if(style == KAMITE):
        CharaOut(0.4, WAIT, 120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE):
        CharaOut(0.4, WAIT, -120, 0, CID, CID2, CID3)
    elif(style == TOP):
        CharaOut(0.4, WAIT, 0, 120, CID, CID2, CID3)
    elif(style == BOTTOM):
        CharaOut(0.4, WAIT, 0, -120, CID, CID2, CID3)
    elif(style == KAMITE_REVERSE):
        CharaOut(0.4, REVERSE, 120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE_REVERSE):
        CharaOut(0.4, REVERSE, -120, 0, CID, CID2, CID3)
    elif(style == TOP_REVERSE):
        CharaOut(0.4, REVERSE, 0, 120, CID, CID2, CID3)
    elif(style == BOTTOM_REVERSE):
        CharaOut(0.4, REVERSE, 0, -120, CID, CID2, CID3)
    elif(style == KAMITE_SYNC):
        CharaOut(0.4, SYNC, 120, 0, CID, CID2, CID3)
    elif(style == SHIMOTE_SYNC):
        CharaOut(0.4, SYNC, -120, 0, CID, CID2, CID3)
    elif(style == TOP_SYNC):
        CharaOut(0.4, SYNC, 0, 120, CID, CID2, CID3)
    elif(style == BOTTOM_SYNC):
        CharaOut(0.4, SYNC, 0, -120, CID, CID2, CID3)
    else:
        CharaOut(0.3, SYNC, 0, 0, CID, CID2, CID3)
    wait(0.5)
    set_volume(0, 0.5, SE)

def CharaIn(sec, wait, X, Y, CID, CID2, CID3):
    if(wait == WAIT):
        mnu(CID, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 1, EaseOutSine)
        cmp(CID, sec, X, Y, 1, 1, 0, 1)
        wait(sec)
        if(CID2 == 0):
            pass
        else:
            mnu(CID2, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 1, EaseOutSine)
            cmp(CID2, sec, X, Y, 1, 1, 0, 1)
            wait(sec)
        if(CID3 == 0):
            pass
        else:
            mnu(CID3, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 1, EaseOutSine)
            cmp(CID3, sec, X, Y, 1, 1, 0, 1)
            wait(sec)
    elif(wait == REVERSE):
        if(CID3 == 0):
            pass
        else:
            mnu(CID3, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 1, EaseOutSine)
            cmp(CID3, sec, X, Y, 1, 1, 0, 1)
            wait(sec)
        if(CID2 == 0):
            pass
        else:
            mnu(CID2, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 1, EaseOutSine)
            cmp(CID2, sec, X, Y, 1, 1, 0, 1)
            if(CID3 == 0):
                pass
            else:
                chara_emotion(CID3, 0)
            wait(sec)
        mnu(CID, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 1, EaseOutSine)
        cmp(CID, sec, X, Y, 1, 1, 0, 1)
        if(CID2 == 0):
            pass
        else:
            chara_emotion(CID2, 0)
        if(CID3 == 0):
            pass
        else:
            chara_emotion(CID3, 0)
        wait(sec)
    else:
        mnu(CID, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 1, EaseOutSine)
        cmp(CID, sec, X, Y, 1, 1, 0, 1)
        if(CID2 == 0):
            pass
        else:
            mnu(CID2, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 1, EaseOutSine)
            cmp(CID2, sec, X, Y, 1, 1, 0, 1)
        if(CID3 == 0):
            pass
        else:
            mnu(CID3, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 1, EaseOutSine)
            cmp(CID3, sec, X, Y, 1, 1, 0, 1)
        wait(sec)
    chara_visible(CID, true)
    if(CID2 == 0):
        pass
    else:
        chara_visible(CID2, true)
    if(CID3 == 0):
        pass
    else:
        chara_visible(CID3, true)

def CharaOut(sec, wait, X, Y, CID, CID2, CID3):
    chara_emotion(CID, 0)
    if(CID2 == 0):
        pass
    else:
        chara_emotion(CID2, 0)
    if(CID3 == 0):
        pass
    else:
        chara_emotion(CID3, 0)
    reset_text()
    if(wait == WAIT):
        if(CID3 == 0):
            pass
        else:
            mnu(CID3, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 0, EaseOutSine)
            cmp(CID3, sec, X, Y, 1, 1, 0, 0)
            wait(sec)
        if(CID2 == 0):
            pass
        else:
            mnu(CID2, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 0, EaseOutSine)
            cmp(CID2, sec, X, Y, 1, 1, 0, 0)
            wait(sec)
        mnu(CID, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 0, EaseOutSine)
        cmp(CID, sec, X, Y, 1, 1, 0, 0)
        wait(sec)
    elif(wait == REVERSE):
        mnu(CID, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 0, EaseOutSine)
        cmp(CID, sec, X, Y, 1, 1, 0, 0)
        if(CID2 == 0):
            pass
        else:
            chara_emotion(CID2, 0)
        if(CID3 == 0):
            pass
        else:
            chara_emotion(CID3, 0)
        wait(sec)
        if(CID2 == 0):
            pass
        else:
            mnu(CID2, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 0, EaseOutSine)
            cmp(CID2, sec, X, Y, 1, 1, 0, 0)
            if(CID3 == 0):
                pass
            else:
                chara_emotion(CID3, 0)
            wait(sec)
        if(CID3 == 0):
            pass
        else:
            mnu(CID3, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 0, EaseOutSine)
            cmp(CID3, sec, X, Y, 1, 1, 0, 0)
            wait(sec)
    else:
        if(CID3 == 0):
            pass
        else:
            mnu(CID3, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 0, EaseOutSine)
            cmp(CID3, sec, X, Y, 1, 1, 0, 0)
        if(CID2 == 0):
            pass
        else:
            mnu(CID2, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 0, EaseOutSine)
            cmp(CID2, sec, X, Y, 1, 1, 0, 0)
        mnu(CID, true, sec, X, Y, EaseOutSine, sec, 1, 1, 1, sec, 0, 1, sec, 0, EaseOutSine)
        cmp(CID, sec, X, Y, 1, 1, 0, 0)
        wait(sec)
    chara_visible(CID, false)
    eyeblink(CID)
    lipsynch(CID)
    if(CID2 == 0):
        pass
    else:
        chara_visible(CID2, false)
        eyeblink(CID2)
        lipsynch(CID2)
    if(CID3 == 0):
    else:
        chara_visible(CID3, false)
        eyeblink(CID3)
        lipsynch(CID3)

