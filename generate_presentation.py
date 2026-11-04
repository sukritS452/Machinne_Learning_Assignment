"""
Generates a polished 6-slide presentation in PPTX format for the Machine Learning Assignment.
Author: Sukriti Sapkota (ID: 260180)
"""

import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation(output_path):
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Global Color Palette
    BG_COLOR = RGBColor(248, 250, 252)        # Soft slate off-white #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)         # Pure White #FFFFFF
    BORDER_COLOR = RGBColor(226, 232, 240)    # Slate 200 #E2E8F0
    TEXT_DARK = RGBColor(15, 23, 42)          # Slate 900 #0F172A
    TEXT_MUTED = RGBColor(100, 116, 139)      # Slate 500 #64748B
    PRIMARY_GREEN = RGBColor(5, 150, 105)     # Emerald 600 #059669
    PRIMARY_BLUE = RGBColor(37, 99, 235)      # Blue 600 #2563EB
    PRIMARY_PURPLE = RGBColor(124, 58, 237)   # Purple 600 #7C3AED
    ACCENT_AMBER = RGBColor(217, 119, 6)      # Amber 600 #D97706
    NAVY_HEADER = RGBColor(30, 41, 59)        # Slate 800 #1E293B

    img_dir = r"c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment\Sukriti_Sapkota_260180_LaTeX\output_image"

    def apply_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text, tag_color=PRIMARY_GREEN):
        # Top Accent Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.38), Inches(3.0), Inches(0.30))
        badge.fill.solid()
        badge.fill.fore_color.rgb = tag_color
        badge.line.fill.background()
        tf_b = badge.text_frame
        tf_b.word_wrap = False
        p_b = tf_b.paragraphs[0]
        p_b.text = tag_text.upper()
        p_b.font.size = Pt(9.0)
        p_b.font.bold = True
        p_b.font.color.rgb = RGBColor(255, 255, 255)
        p_b.alignment = PP_ALIGN.CENTER

        # Slide Title
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.72))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = NAVY_HEADER

        p2 = tf.add_paragraph()
        p2.text = subtitle_text
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_COLOR):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        return card

    # =========================================================================
    # SLIDE 1: Title & Executive Architecture Overview
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_background(s1)

    # Top Pill
    pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.55), Inches(4.8), Inches(0.35))
    pill.fill.solid()
    pill.fill.fore_color.rgb = PRIMARY_BLUE
    pill.line.fill.background()
    p_pill = pill.text_frame.paragraphs[0]
    p_pill.text = "MACHINE LEARNING ASSIGNMENT | ACADEMIC YEAR 2026"
    p_pill.font.size = Pt(9.5)
    p_pill.font.bold = True
    p_pill.font.color.rgb = RGBColor(255, 255, 255)
    p_pill.alignment = PP_ALIGN.CENTER

    # Title & Subtitle Box
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.02), Inches(5.9), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = 0
    p1 = tf1.paragraphs[0]
    p1.text = "Longitudinal Agro-Climatic Dynamics & Machine Learning Crop Yield Prediction"
    p1.font.size = Pt(23)
    p1.font.bold = True
    p1.font.color.rgb = NAVY_HEADER

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Multi-Model Supervised Benchmarking, Unsupervised Ecological Regimes, and Real-Time Decision-Support GUI"
    p1_sub.font.size = Pt(11)
    p1_sub.font.color.rgb = PRIMARY_GREEN
    p1_sub.font.bold = True
    p1_sub.space_before = Pt(6)

    # Metadata Card
    c_meta = add_card(s1, Inches(0.8), Inches(3.35), Inches(5.8), Inches(1.85))
    tb_m = s1.shapes.add_textbox(Inches(1.0), Inches(3.45), Inches(5.4), Inches(1.65))
    tf_meta = tb_m.text_frame
    tf_meta.word_wrap = True
    tf_meta.margin_left = tf_meta.margin_right = tf_meta.margin_top = tf_meta.margin_bottom = 0
    p_m1 = tf_meta.paragraphs[0]
    p_m1.text = "PRESENTER & PROJECT CREDENTIALS"
    p_m1.font.size = Pt(9.5)
    p_m1.font.bold = True
    p_m1.font.color.rgb = PRIMARY_BLUE

    items = [
        ("Student Name:", "Sukriti Sapkota"),
        ("Student ID:", "260180"),
        ("Dataset Archive:", "11,210 Observations | 75 Districts | 32 Years (1982–2013)"),
        ("Analyzed Crops:", "Paddy, Maize, Wheat, Millet, and Barley")
    ]
    for lbl, val in items:
        p_row = tf_meta.add_paragraph()
        run1 = p_row.add_run()
        run1.text = f"{lbl} "
        run1.font.bold = True
        run1.font.size = Pt(10)
        run1.font.color.rgb = TEXT_DARK
        run2 = p_row.add_run()
        run2.text = val
        run2.font.size = Pt(10)
        run2.font.color.rgb = TEXT_MUTED

    # Bottom Badges
    badges = [
        ("4 ML Classifiers", PRIMARY_GREEN),
        ("K-Means & PCA (k=3)", PRIMARY_PURPLE),
        ("Ridge OLS Baseline", PRIMARY_BLUE),
        ("Tkinter GUI Dashboard", ACCENT_AMBER)
    ]
    bx = Inches(0.8)
    for b_title, b_color in badges:
        b_shp = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, Inches(5.45), Inches(1.35), Inches(0.42))
        b_shp.fill.solid()
        b_shp.fill.fore_color.rgb = b_color
        b_shp.line.fill.background()
        tf_b = b_shp.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = b_title
        p_b.font.size = Pt(8.5)
        p_b.font.bold = True
        p_b.font.color.rgb = RGBColor(255, 255, 255)
        p_b.alignment = PP_ALIGN.CENTER
        bx += Inches(1.48)

    # Right Image: Problem Statement Architecture
    img1_path = os.path.join(img_dir, "problem_statement_architecture.jpg")
    if os.path.exists(img1_path):
        add_card(s1, Inches(6.8), Inches(0.55), Inches(5.75), Inches(5.35))
        s1.shapes.add_picture(img1_path, Inches(6.9), Inches(0.65), Inches(5.55), Inches(5.15))
        
        cap_box = s1.shapes.add_textbox(Inches(6.8), Inches(6.0), Inches(5.75), Inches(0.7))
        tf_cap = cap_box.text_frame
        tf_cap.word_wrap = True
        p_cap = tf_cap.paragraphs[0]
        p_cap.text = "Figure 1: End-to-End Problem Formulation & Solution Architecture: Connecting field vulnerabilities, foundational literature gaps, and machine learning pipelines."
        p_cap.font.size = Pt(9)
        p_cap.font.italic = True
        p_cap.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 2: Research Context, Literature Gap Analysis & Methodology
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_background(s2)
    add_header(s2, "01. Literature Critique & Contributions",
               "Agronomic Problem Formulation & Literature Gap Critique",
               "Overcoming the limitations of national spatial smoothing and data-scarce satellite pipelines")

    # Left Column: Gaps in Literature
    add_card(s2, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.5))
    tb_g = s2.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(5.2), Inches(5.2))
    tf_gaps = tb_g.text_frame
    tf_gaps.word_wrap = True
    tf_gaps.margin_left = tf_gaps.margin_right = tf_gaps.margin_top = tf_gaps.margin_bottom = 0
    
    p_g_title = tf_gaps.paragraphs[0]
    p_g_title.text = "CRITICAL GAPS IN FOUNDATIONAL LITERATURE"
    p_g_title.font.size = Pt(11)
    p_g_title.font.bold = True
    p_g_title.font.color.rgb = PRIMARY_BLUE

    gaps = [
        ("Base Paper 1 (Dhakal & Dhungana, 2023) [1]:",
         "Evaluated 6 ML models on 49-year cereal yields.\n"
         "• CRITICAL GAP: Modeled macro-level nationally aggregated data, concealing localized district micro-climatic shocks and lacking spatial cluster profiling."),
        ("Base Paper 2 (Crane-Droesch, 2018) [2]:",
         "Semiparametric neural networks on US Corn Belt.\n"
         "• CRITICAL GAP: Confined to mechanized, homogeneous US monoculture; unconstrained neural nets diverge on extreme climate anomalies without physical bounds."),
        ("Base Paper 3 (Fernandez-Beltran et al., 2021) [3]:",
         "3D-CNN on Sentinel-2 optical satellite data.\n"
         "• CRITICAL GAP: Spanned only 3 years (missing decadal oscillations) and suffered heavy data loss during cloudy monsoon seasons.")
    ]

    for title, desc in gaps:
        p_t = tf_gaps.add_paragraph()
        p_t.text = title
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = NAVY_HEADER
        p_t.space_before = Pt(6)

        p_d = tf_gaps.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_MUTED

    # Right Column: Framework Architecture Picture
    img2_path = os.path.join(img_dir, "fig1_framework_architecture.png")
    if os.path.exists(img2_path):
        add_card(s2, Inches(6.7), Inches(1.5), Inches(5.8), Inches(3.2))
        s2.shapes.add_picture(img2_path, Inches(6.8), Inches(1.6), Inches(5.6), Inches(3.0))

    # Right Bottom Card: Our Methodological Contributions
    add_card(s2, Inches(6.7), Inches(4.85), Inches(5.8), Inches(2.15))
    tb_c = s2.shapes.add_textbox(Inches(6.9), Inches(4.98), Inches(5.4), Inches(1.95))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = tf_c.margin_right = tf_c.margin_top = tf_c.margin_bottom = 0
    p_c_t = tf_c.paragraphs[0]
    p_c_t.text = "CORE METHODOLOGICAL CONTRIBUTIONS OF OUR WORK"
    p_c_t.font.size = Pt(10.5)
    p_c_t.font.bold = True
    p_c_t.font.color.rgb = PRIMARY_GREEN

    c_points = [
        "1. Longitudinal Multi-District Integration: 32-year disaggregated district-level records.",
        "2. In-Notebook Data Cleansing: Automated outlier removal, imputation & validation in Python.",
        "3. Non-Linear Feature Engineering: De Martonne Aridity [4], Thermal Range & Moisture Stress.",
        "4. Unsupervised Zoning: PCA & K-Means (k=3) identifying distinct agro-ecological regimes."
    ]
    for cp in c_points:
        p_cp = tf_c.add_paragraph()
        p_cp.text = cp
        p_cp.font.size = Pt(9.5)
        p_cp.font.color.rgb = TEXT_DARK
        p_cp.space_before = Pt(3)

    # =========================================================================
    # SLIDE 3: Unsupervised Agro-Climatic Zoning (PCA & K-Means)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_background(s3)
    add_header(s3, "02. Unsupervised Learning",
               "Unsupervised Agro-Climatic Zoning (PCA & K-Means Clustering)",
               "Objective spatial-environmental stratification validated by Elbow and Silhouette metrics")

    # Top KPI Metric Cards
    kpis = [
        ("PCA Variance Explained", "68.42%", "Top 3 Components (PC1: Climate, PC2: Elevation, PC3: Shear)", PRIMARY_BLUE),
        ("Optimal Cluster Count", "k = 3", "WCSS Elbow curve bend + domain agro-climatic alignment", PRIMARY_PURPLE),
        ("Peak Silhouette Score", "0.3298", "Davies-Bouldin Index: 1.1450 (Strong separation)", PRIMARY_GREEN)
    ]
    kx = Inches(0.8)
    for title, val, sub, col in kpis:
        c_k = add_card(s3, kx, Inches(1.5), Inches(3.7), Inches(1.15))
        tb_k = s3.shapes.add_textbox(kx + Inches(0.15), Inches(1.58), Inches(3.4), Inches(0.95))
        tf_k = tb_k.text_frame
        tf_k.word_wrap = True
        tf_k.margin_left = tf_k.margin_right = tf_k.margin_top = tf_k.margin_bottom = 0
        p_t = tf_k.paragraphs[0]
        p_t.text = title.upper()
        p_t.font.size = Pt(8.5)
        p_t.font.bold = True
        p_t.font.color.rgb = col

        p_v = tf_k.add_paragraph()
        p_v.text = val
        p_v.font.size = Pt(20)
        p_v.font.bold = True
        p_v.font.color.rgb = NAVY_HEADER

        p_s = tf_k.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(8)
        p_s.font.color.rgb = TEXT_MUTED
        kx += Inches(3.9)

    # Left: 3 Delineated Agro-Ecological Regimes
    add_card(s3, Inches(0.8), Inches(2.8), Inches(5.6), Inches(4.25))
    tb_reg = s3.shapes.add_textbox(Inches(1.0), Inches(2.95), Inches(5.2), Inches(3.95))
    tf_reg = tb_reg.text_frame
    tf_reg.word_wrap = True
    tf_reg.margin_left = tf_reg.margin_right = tf_reg.margin_top = tf_reg.margin_bottom = 0
    p_r_t = tf_reg.paragraphs[0]
    p_r_t.text = "CHARACTERISTICS OF DELINEATED AGRO-ECOLOGICAL REGIMES"
    p_r_t.font.size = Pt(10.5)
    p_r_t.font.bold = True
    p_r_t.font.color.rgb = PRIMARY_GREEN

    regimes_info = [
        ("Cluster 0: Lowland Sub-Tropical (High Yield)",
         "• Mean Yield: 1,669.91 kg/ha | Warm temperatures & high monsoon rainfall.\n"
         "• Agronomic Focus: Primary grain basket (paddy & maize); high humidity.\n"
         "• Vulnerability: Flood inundation and post-monsoon waterlogging.",
         PRIMARY_GREEN),
        ("Cluster 1: Mid-Hills Temperate (Moderate Yield)",
         "• Mean Yield: 1,554.06 kg/ha | Moderate elevation, optimal thermal stability.\n"
         "• Agronomic Focus: Mixed cropping (wheat, millet, maize); terraced cultivation.\n"
         "• Vulnerability: Seasonal drought cycles and erratic rainfall onset.",
         PRIMARY_BLUE),
        ("Cluster 2: Highland Alpine (Low Yield)",
         "• Mean Yield: 1,313.74 kg/ha | High elevation, low atmospheric pressure & thermal deficit.\n"
         "• Agronomic Focus: Cold-hardy crops (barley & finger millet); shorter growing seasons.\n"
         "• Vulnerability: Severe frost damage and extreme evapotranspiration deficits.",
         ACCENT_AMBER)
    ]

    for r_title, r_body, r_col in regimes_info:
        p_rt = tf_reg.add_paragraph()
        p_rt.text = r_title
        p_rt.font.size = Pt(9.5)
        p_rt.font.bold = True
        p_rt.font.color.rgb = r_col
        p_rt.space_before = Pt(5)

        p_rb = tf_reg.add_paragraph()
        p_rb.text = r_body
        p_rb.font.size = Pt(8.5)
        p_rb.font.color.rgb = TEXT_DARK

    # Right: Embedded PCA & Cluster Visual
    img4_path = os.path.join(img_dir, "fig4_pca_and_clusters.png")
    if os.path.exists(img4_path):
        add_card(s3, Inches(6.7), Inches(2.8), Inches(5.8), Inches(4.25))
        s3.shapes.add_picture(img4_path, Inches(6.8), Inches(3.0), Inches(5.6), Inches(3.8))

    # =========================================================================
    # SLIDE 4: Supervised Classification & Continuous Regression Benchmark
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_background(s4)
    add_header(s4, "03. Supervised Modeling & Evaluation",
               "Multi-Model Supervised Classification & Baseline Regression",
               "Evaluating 4 algorithmic paradigms across balanced productivity tiers (Low, Medium, High)")

    # Left: Benchmark Results Card Container
    add_card(s4, Inches(0.8), Inches(1.5), Inches(6.0), Inches(5.5))
    
    # Dedicated Title Box above Table
    tb_t_title = s4.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(5.6), Inches(0.35))
    tf_th = tb_t_title.text_frame
    tf_th.word_wrap = True
    tf_th.margin_left = tf_th.margin_right = tf_th.margin_top = tf_th.margin_bottom = 0
    p_th = tf_th.paragraphs[0]
    p_th.text = "EMPIRICAL MODEL EVALUATION & BENCHMARK MATRIX"
    p_th.font.size = Pt(11)
    p_th.font.bold = True
    p_th.font.color.rgb = PRIMARY_BLUE

    # Create table shape on slide
    rows, cols = 5, 4
    table_shape = s4.shapes.add_table(rows, cols, Inches(1.0), Inches(2.05), Inches(5.6), Inches(2.1))
    table = table_shape.table
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(1.1)
    table.columns[2].width = Inches(1.1)
    table.columns[3].width = Inches(1.2)

    headers = ["Algorithm", "Accuracy", "F1-Score", "AUC-ROC"]
    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_HEADER
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    data = [
        ("Random Forest (Ensemble)", "63.63%", "63.67%", "0.8168", True),
        ("Decision Tree (CART)", "61.13%", "61.11%", "0.7251", False),
        ("Multinomial Logistic Reg.", "56.67%", "56.57%", "0.7490", False),
        ("Support Vector Machine (RBF)", "53.90%", "53.71%", "0.7302", False),
    ]

    for row_idx, (m_name, acc, f1, auc, is_best) in enumerate(data, 1):
        row_vals = [m_name, acc, f1, auc]
        for col_idx, val in enumerate(row_vals):
            cell = table.cell(row_idx, col_idx)
            cell.text = val
            cell.fill.solid()
            if is_best:
                cell.fill.fore_color.rgb = RGBColor(236, 253, 245) # Light emerald tint
            else:
                cell.fill.fore_color.rgb = RGBColor(255, 255, 255)
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9)
            if is_best:
                p.font.bold = True
                p.font.color.rgb = PRIMARY_GREEN
            else:
                p.font.color.rgb = TEXT_DARK
            if col_idx > 0:
                p.alignment = PP_ALIGN.CENTER

    # Summary Box below table
    sum_box = s4.shapes.add_textbox(Inches(1.0), Inches(4.35), Inches(5.6), Inches(2.4))
    tf_sum = sum_box.text_frame
    tf_sum.word_wrap = True
    tf_sum.margin_left = tf_sum.margin_right = tf_sum.margin_top = tf_sum.margin_bottom = 0
    p_s1 = tf_sum.paragraphs[0]
    p_s1.text = "KEY EMPIRICAL FINDINGS & REGRESSION BASELINE:"
    p_s1.font.size = Pt(10)
    p_s1.font.bold = True
    p_s1.font.color.rgb = PRIMARY_GREEN

    points = [
        ("Random Forest Superiority: ", "Achieved peak AUC-ROC of 0.8168 and 63.63% test accuracy, effectively resolving non-linear environmental interactions without overfitting."),
        ("Decision Tree Overfitting: ", "CART achieved 100% training accuracy but dropped to 61.13% on hold-out testing due to single-tree structural variance."),
        ("Continuous Ridge OLS Baseline: ", "Achieved R² = 0.3842 and RMSE = 624.38 kg/ha. Proved linear parametric models capture macro elevation but fail non-linear heat shock thresholds.")
    ]
    for lbl, desc in points:
        p = tf_sum.add_paragraph()
        p.space_before = Pt(3)
        run1 = p.add_run()
        run1.text = f"• {lbl}"
        run1.font.bold = True
        run1.font.size = Pt(8.5)
        run1.font.color.rgb = TEXT_DARK
        run2 = p.add_run()
        run2.text = desc
        run2.font.size = Pt(8.5)
        run2.font.color.rgb = TEXT_MUTED

    # Right: Confusion Matrices Image
    img5_path = os.path.join(img_dir, "fig5_confusion_matrices.png")
    if os.path.exists(img5_path):
        add_card(s4, Inches(7.0), Inches(1.5), Inches(5.5), Inches(5.5))
        s4.shapes.add_picture(img5_path, Inches(7.1), Inches(1.6), Inches(5.3), Inches(5.3))

    # =========================================================================
    # SLIDE 5: Feature Sensitivity & Computational Complexity Analysis
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_background(s5)
    add_header(s5, "04. Sensitivity & Complexity",
               "Environmental Feature Attribution & Big-O Computational Complexity",
               "Identifying dominant climate drivers and profiling real-time hardware execution latency")

    # Left Card: Feature Sensitivity
    add_card(s5, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.5))
    tb_ft = s5.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(5.2), Inches(0.35))
    tf_ft = tb_ft.text_frame
    tf_ft.word_wrap = True
    tf_ft.margin_left = tf_ft.margin_right = tf_ft.margin_top = tf_ft.margin_bottom = 0
    p_f_t = tf_ft.paragraphs[0]
    p_f_t.text = "AGRONOMIC FEATURE ATTRIBUTION (GINI IMPORTANCE)"
    p_f_t.font.size = Pt(10.5)
    p_f_t.font.bold = True
    p_f_t.font.color.rgb = PRIMARY_GREEN

    # Image Feature Importance
    img6_path = os.path.join(img_dir, "fig6_feature_importance.png")
    if os.path.exists(img6_path):
        s5.shapes.add_picture(img6_path, Inches(1.0), Inches(2.05), Inches(5.2), Inches(2.7))

    # Bullets below image
    f_desc_box = s5.shapes.add_textbox(Inches(1.0), Inches(4.88), Inches(5.2), Inches(1.95))
    tf_fd = f_desc_box.text_frame
    tf_fd.word_wrap = True
    tf_fd.margin_left = tf_fd.margin_right = tf_fd.margin_top = tf_fd.margin_bottom = 0
    f_bullets = [
        ("Moisture Stress (0.166): ", "Primary driver of crop failure; captures compound heat-dryness exposure during flowering."),
        ("De Martonne Aridity (0.134): ", "Non-linear threshold separator discriminating arid stress from optimal vegetative moisture."),
        ("Mean Temperature (0.118): ", "Elevation-linked thermal energy driver governing physiological maturation cycles.")
    ]
    for lbl, bld in f_bullets:
        p = tf_fd.add_paragraph() if tf_fd.paragraphs[0].text else tf_fd.paragraphs[0]
        p.space_before = Pt(3)
        r1 = p.add_run()
        r1.text = f"• {lbl}"
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = TEXT_DARK
        r2 = p.add_run()
        r2.text = bld
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_MUTED

    # Right Card: Complexity Benchmarks
    add_card(s5, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.5))
    tb_cpt = s5.shapes.add_textbox(Inches(6.9), Inches(1.65), Inches(5.4), Inches(0.35))
    tf_cpt = tb_cpt.text_frame
    tf_cpt.word_wrap = True
    tf_cpt.margin_left = tf_cpt.margin_right = tf_cpt.margin_top = tf_cpt.margin_bottom = 0
    p_cp_t = tf_cpt.paragraphs[0]
    p_cp_t.text = "THEORETICAL DERIVATION & HARDWARE EXECUTION PROFILE"
    p_cp_t.font.size = Pt(10.5)
    p_cp_t.font.bold = True
    p_cp_t.font.color.rgb = PRIMARY_BLUE

    # Image Complexity Benchmark
    img8_path = os.path.join(img_dir, "fig8_time_complexity_benchmark.png")
    if os.path.exists(img8_path):
        s5.shapes.add_picture(img8_path, Inches(6.9), Inches(2.05), Inches(5.4), Inches(2.55))

    # Bullets below complexity image
    c_desc_box = s5.shapes.add_textbox(Inches(6.9), Inches(4.8), Inches(5.4), Inches(2.0))
    tf_cd = c_desc_box.text_frame
    tf_cd.word_wrap = True
    tf_cd.margin_left = tf_cd.margin_right = tf_cd.margin_top = tf_cd.margin_bottom = 0
    comp_bullets = [
        ("Random Forest: ", "Training: O(M · K · N log N) [18.42 s] | Inference: 0.082 ms/sample | Memory: 5.07 MB. Sub-millisecond latency enables real-time decision support."),
        ("Support Vector Machine: ", "Training: O(N³) [4.12 s] | Severe cubic scaling bottleneck on large observational datasets."),
        ("Multinomial Logistic Reg: ", "Training: O(N · D · K) [0.18 s] | Near-instantaneous convergence but constrained by linear boundary assumptions.")
    ]
    for lbl, bld in comp_bullets:
        p = tf_cd.add_paragraph() if tf_cd.paragraphs[0].text else tf_cd.paragraphs[0]
        p.space_before = Pt(3)
        r1 = p.add_run()
        r1.text = f"• {lbl}"
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = TEXT_DARK
        r2 = p.add_run()
        r2.text = bld
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 6: Interactive GUI Dashboard, Governance & Conclusion
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_background(s6)
    add_header(s6, "05. GUI Deployment & Impact",
               "Interactive Decision-Support Dashboard, Governance & Conclusion",
               "Bridging machine learning insights to regional agricultural extension officers and farmers")

    # Left: Dashboard Screenshot Card
    add_card(s6, Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.5))
    
    tb_db_t = s6.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(6.4), Inches(0.35))
    tf_dbt = tb_db_t.text_frame
    tf_dbt.word_wrap = True
    tf_dbt.margin_left = tf_dbt.margin_right = tf_dbt.margin_top = tf_dbt.margin_bottom = 0
    p_dbt = tf_dbt.paragraphs[0]
    p_dbt.text = "STANDALONE TKINTER INTERACTIVE DECISION-SUPPORT GUI"
    p_dbt.font.size = Pt(10.5)
    p_dbt.font.bold = True
    p_dbt.font.color.rgb = PRIMARY_BLUE

    img9_path = os.path.join(img_dir, "fig9_dashboard_overview.png")
    if os.path.exists(img9_path):
        s6.shapes.add_picture(img9_path, Inches(1.0), Inches(2.05), Inches(6.4), Inches(4.0))

        # Dashboard features bar
        db_desc = s6.shapes.add_textbox(Inches(1.0), Inches(6.15), Inches(6.4), Inches(0.75))
        tf_db = db_desc.text_frame
        tf_db.word_wrap = True
        tf_db.margin_left = tf_db.margin_right = tf_db.margin_top = tf_db.margin_bottom = 0
        p_db = tf_db.paragraphs[0]
        p_db.text = "Operational Features: Multi-District / Crop Filters • Real-Time Yield Predictor • Embedded Matplotlib Visuals • Dynamic KPI Stat Cards • Non-Blocking Multi-Threaded Engine."
        p_db.font.size = Pt(8.5)
        p_db.font.bold = True
        p_db.font.color.rgb = PRIMARY_GREEN

    # Right: Social, Ethical, Professional Governance & Final Conclusion
    add_card(s6, Inches(7.8), Inches(1.5), Inches(4.7), Inches(5.5))
    tb_gov = s6.shapes.add_textbox(Inches(8.0), Inches(1.65), Inches(4.3), Inches(5.2))
    tf_gov = tb_gov.text_frame
    tf_gov.word_wrap = True
    tf_gov.margin_left = tf_gov.margin_right = tf_gov.margin_top = tf_gov.margin_bottom = 0
    p_gov_t = tf_gov.paragraphs[0]
    p_gov_t.text = "ETHICAL GOVERNANCE & PROJECT CONCLUSION"
    p_gov_t.font.size = Pt(10.5)
    p_gov_t.font.bold = True
    p_gov_t.font.color.rgb = PRIMARY_GREEN

    gov_points = [
        ("Algorithmic Fairness & Smallholder Protection:",
         "Avoided commercial reporting bias by standardizing district records, ensuring remote high-elevation smallholders are not neglected in regional grain supply planning."),
        ("Interpretability & Transparency:",
         "Provided transparent Gini impurity and threshold indicators to extension officers rather than deploying black-box predictions."),
        ("Data Provenance & Integrity:",
         "Eliminated recording ledger anomalies and zero-yield logging errors via in-notebook automated preprocessing pipelines."),
        ("Final Project Summary:",
         "Successfully delivered an end-to-end framework combining 32 years of data, unsupervised agro-zoning (k=3), superior Random Forest classification (0.8168 AUC-ROC), and an interactive GUI for real-time proactive food security planning.")
    ]

    for title, desc in gov_points:
        p = tf_gov.add_paragraph()
        p.text = title
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = NAVY_HEADER
        p.space_before = Pt(5)

        pd = tf_gov.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(8.5)
        pd.font.color.rgb = TEXT_MUTED

    prs.save(output_path)
    print(f"Presentation successfully saved to {output_path}")

if __name__ == "__main__":
    out1 = r"c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment\ML_Crop_Dynamics_Presentation_Sukriti_260180.pptx"
    out2 = r"c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment\Assignment\ML_Crop_Dynamics_Presentation_Sukriti_260180.pptx"
    build_presentation(out1)
    build_presentation(out2)
