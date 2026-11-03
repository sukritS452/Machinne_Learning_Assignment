import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

def generate_problem_statement_figure():
    # Set high resolution figure
    fig_w, fig_h = 20, 11.25  # 16:9 ratio
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=300)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 11.25)
    ax.axis('off')

    # Background canvas
    bg_rect = patches.Rectangle((0, 0), 20, 11.25, facecolor='#0F172A', edgecolor='none')
    ax.add_patch(bg_rect)

    # Inner soft container
    inner_card = patches.FancyBboxPatch(
        (0.4, 0.4), 19.2, 10.45,
        boxstyle="round,pad=0.0,rounding_size=0.25",
        facecolor='#F8FAFC',
        edgecolor='#334155',
        linewidth=1.5
    )
    ax.add_patch(inner_card)

    # ----------------------------------------------------
    # HEADER BANNER
    # ----------------------------------------------------
    header_banner = patches.FancyBboxPatch(
        (0.6, 9.4), 18.8, 1.25,
        boxstyle="round,pad=0.0,rounding_size=0.18",
        facecolor='#1E293B',
        edgecolor='#0284C7',
        linewidth=2.0
    )
    ax.add_patch(header_banner)

    # Decorative accent line on header
    ax.plot([0.8, 19.2], [9.45, 9.45], color='#38BDF8', linewidth=3, alpha=0.9)

    ax.text(
        10.0, 10.28,
        "AGRICULTURAL CROP YIELD & AGRO-CLIMATIC DYNAMICS: PROBLEM FORMULATION & SOLUTION ARCHITECTURE",
        ha='center', va='center', color='#F8FAFC', fontsize=14.5, weight='bold'
    )
    ax.text(
        10.0, 9.85,
        "Author: Sukriti Sapkota (ID: 260180)  |  MSc Data Science & Computational Intelligence (STW7072CEM)  |  Coventry University / Softwarica College",
        ha='center', va='center', color='#94A3B8', fontsize=10.5, weight='semibold'
    )
    ax.text(
        10.0, 9.58,
        "Study Domain: 75 Administrative Sub-Regions  •  32 Consecutive Cropping Years (1982–2013)  •  5 Staple Cereals  •  11,210 Audited Records",
        ha='center', va='center', color='#38BDF8', fontsize=9.5, weight='bold'
    )

    # ----------------------------------------------------
    # 4 COLUMN DEFINITIONS
    # ----------------------------------------------------
    cols = [
        {
            "num": "01",
            "title": "AGRONOMIC REALITY &\nVULNERABILITIES",
            "subtitle": "The Agronomic Problem Domain",
            "color": "#DC2626",      # Crimson
            "light_bg": "#FEF2F2",
            "border": "#FCA5A5",
            "x": 0.65, "w": 4.35,
            "cards": [
                {
                    "tag": "CHALLENGE 1",
                    "heading": "Topographical Heterogeneity",
                    "bullets": [
                        "Elevation ranges from lowland floodplains (<300m) to alpine mountain valleys (>2500m).",
                        "Heterogeneous microclimates create stark yield disparities within short geographic spans.",
                        "Uniform agrarian policy fails to address localized micro-ecological pockets."
                    ]
                },
                {
                    "tag": "CHALLENGE 2",
                    "heading": "Climate Volatility & Thresholds",
                    "bullets": [
                        "Rising ambient heat, erratic monsoon rainfall, and sudden post-monsoon deluges.",
                        "Compounded stress: Thermal spikes co-occurring with vapor pressure deficit induce floral sterility.",
                        "Linear models fundamentally miss these critical physiological heat thresholds."
                    ]
                },
                {
                    "tag": "CHALLENGE 3",
                    "heading": "Smallholder Food Security Risk",
                    "bullets": [
                        "80%+ subsistence cereal production (Paddy, Maize, Wheat, Millet, Barley) is strictly rainfed.",
                        "Absence of predictive yield diagnostic tools creates acute vulnerability to climate shocks."
                    ]
                }
            ]
        },
        {
            "num": "02",
            "title": "RESEARCH GAPS IN\nPRIOR LITERATURE",
            "subtitle": "Critical Appraisal of Base Papers",
            "color": "#D97706",      # Amber
            "light_bg": "#FFFBEB",
            "border": "#FCD34D",
            "x": 5.30, "w": 4.35,
            "cards": [
                {
                    "tag": "BASE PAPER 1 (Dhakal, 2023)",
                    "heading": "Spatial Smoothing Bias",
                    "bullets": [
                        "Analyzed 49-year archive using RF, SVM, DT, and Neural Networks on tabular data.",
                        "Critical Limitation: Relied entirely on national macro-aggregates, averaging out local droughts.",
                        "No spatial clustering or multi-variable agro-ecological regime profiling."
                    ]
                },
                {
                    "tag": "BASE PAPER 2 (Crane, 2018)",
                    "heading": "Temperate Monoculture Bias",
                    "bullets": [
                        "Developed semiparametric neural networks under CMIP5 RCP climate trajectories.",
                        "Critical Limitation: Evaluated solely on capital-intensive US Corn Belt monoculture.",
                        "Assumptions fail in fragmented, multi-crop, high-elevation smallholder landscapes."
                    ]
                },
                {
                    "tag": "BASE PAPER 3 (Fernandez, 2021)",
                    "heading": "Temporal & Optical Constraints",
                    "bullets": [
                        "Applied 3D-CNNs to Sentinel-2 satellite imagery for seasonal phenological stages.",
                        "Critical Limitation: Narrow 3-year window (2016–2018) misses decadal climate trends.",
                        "Heavy monsoon cloud cover causes severe optical data dropouts."
                    ]
                }
            ]
        },
        {
            "num": "03",
            "title": "METHODOLOGICAL\nSOLUTION FRAMEWORK",
            "subtitle": "Proposed Machine Learning Pipeline",
            "color": "#2563EB",      # Royal Blue
            "light_bg": "#EFF6FF",
            "border": "#93C5FD",
            "x": 9.95, "w": 4.35,
            "cards": [
                {
                    "tag": "PILLAR 1: INGESTION & CLEANING",
                    "heading": "In-Notebook Data Cleansing",
                    "bullets": [
                        "Strict coursework compliance: automated raw cleansing executed entirely within code.",
                        "Isolates uncultivated records (Area<=10ha) & historical paper ledger typos (>8000 kg/ha).",
                        "Retains 11,210 verified samples (96.4% retention)."
                    ]
                },
                {
                    "tag": "PILLAR 2: FEATURE ENGINEERING",
                    "heading": "Agro-Climatic Indicators",
                    "bullets": [
                        "Thermal Range (ΔT = Tmax - Tmin) capturing diurnal vegetative chilling/heat shock.",
                        "De Martonne Aridity Index (Precip / (Temp + 10)) modeling effective moisture demand.",
                        "Moisture Stress Interaction (RH * SH / 10) capturing atmospheric vapor saturation."
                    ]
                },
                {
                    "tag": "PILLAR 3: MACHINE LEARNING PIPELINE",
                    "heading": "Hybrid Clustering & Classification",
                    "bullets": [
                        "Unsupervised: SVD-PCA (68.4% variance) + K-Means (k=3, Silhouette 0.3298, DB 1.145).",
                        "Supervised: Random Forest (63.63% Acc, 0.8168 AUC) vs DT (61.1%), LogReg (56.7%), SVM (53.9%).",
                        "Parametric Baseline: Ridge Linear Regression (R² = 0.3842, RMSE 624 kg/ha)."
                    ]
                }
            ]
        },
        {
            "num": "04",
            "title": "OPERATIONAL IMPACT &\nPOLICY VALUE",
            "subtitle": "Delivering Practical Value",
            "color": "#059669",      # Emerald Green
            "light_bg": "#ECFDF5",
            "border": "#6EE7B7",
            "x": 14.60, "w": 4.75,
            "cards": [
                {
                    "tag": "OUTCOME 1: SPATIAL ZONING",
                    "heading": "Objective Ecological Zones",
                    "bullets": [
                        "Zone 0: Lowland Sub-Tropical (23.8°C, 1620mm, 1670 kg/ha, Paddy/Maize).",
                        "Zone 1: Mid-Hills Temperate (18.4°C, 1480mm, 1554 kg/ha, Wheat/Maize).",
                        "Zone 2: Highland Alpine (11.2°C, 920mm, 1314 kg/ha, Barley/Millet)."
                    ]
                },
                {
                    "tag": "OUTCOME 2: ACTIONABLE FORESIGHT",
                    "heading": "Pre-Harvest Yield Tier Warning",
                    "bullets": [
                        "Accurately classifies Low, Medium, and High Yield productivity months before harvest.",
                        "Enables targeted release of emergency grain reserves and seasonal micro-credit.",
                        "Guides optimal fertilizer and drought-resistant seed allocation by district."
                    ]
                },
                {
                    "tag": "OUTCOME 3: FIELD DEPLOYABILITY",
                    "heading": "Computational Feasibility",
                    "bullets": [
                        "Sub-millisecond inference latency (0.082 ms/sample) and lightweight 5 MB footprint.",
                        "Interactive Plotly dashboard panel (dashboard.html) for real-time agronomic exploration."
                    ]
                }
            ]
        }
    ]

    # Draw Columns
    for col in cols:
        cx, cw = col["x"], col["w"]

        # Column background container
        col_box = patches.FancyBboxPatch(
            (cx, 0.65), cw, 8.55,
            boxstyle="round,pad=0.0,rounding_size=0.15",
            facecolor=col["light_bg"],
            edgecolor=col["border"],
            linewidth=1.3
        )
        ax.add_patch(col_box)

        # Column Header Badge
        badge_h = 1.15
        badge_y = 8.05
        head_badge = patches.FancyBboxPatch(
            (cx, badge_y), cw, badge_h,
            boxstyle="round,pad=0.0,rounding_size=0.15",
            facecolor=col["color"],
            edgecolor='none'
        )
        ax.add_patch(head_badge)

        # Step indicator circle
        num_circle = patches.Circle((cx + 0.42, badge_y + 0.58), 0.32, facecolor='#FFFFFF', edgecolor='none')
        ax.add_patch(num_circle)
        ax.text(cx + 0.42, badge_y + 0.58, col["num"], ha='center', va='center', color=col["color"], fontsize=11, weight='bold')

        # Header Titles
        ax.text(cx + 0.88, badge_y + 0.68, col["title"], ha='left', va='center', color='#FFFFFF', fontsize=9.2, weight='bold', linespacing=1.0)
        ax.text(cx + 0.88, badge_y + 0.22, col["subtitle"], ha='left', va='center', color='#F1F5F9', fontsize=7.5, style='italic')

        # Draw Cards within Column
        card_y_positions = [5.60, 3.20, 0.80]
        card_heights = [2.30, 2.25, 2.25]

        for i, card in enumerate(col["cards"]):
            cy = card_y_positions[i]
            ch = card_heights[i]

            card_box = patches.FancyBboxPatch(
                (cx + 0.12, cy), cw - 0.24, ch,
                boxstyle="round,pad=0.0,rounding_size=0.12",
                facecolor='#FFFFFF',
                edgecolor=col["border"],
                linewidth=1.0
            )
            ax.add_patch(card_box)

            # Card Tag Badge
            tag_box = patches.FancyBboxPatch(
                (cx + 0.22, cy + ch - 0.34), cw - 0.44, 0.26,
                boxstyle="round,pad=0.0,rounding_size=0.06",
                facecolor=col["color"],
                edgecolor='none',
                alpha=0.12
            )
            ax.add_patch(tag_box)
            ax.text(cx + 0.30, cy + ch - 0.21, card["tag"], ha='left', va='center', color=col["color"], fontsize=7.2, weight='bold')

            # Card Heading
            ax.text(cx + 0.25, cy + ch - 0.56, card["heading"], ha='left', va='center', color='#0F172A', fontsize=8.6, weight='bold')

            # Divider line inside card
            ax.plot([cx + 0.25, cx + cw - 0.25], [cy + ch - 0.72, cy + ch - 0.72], color='#E2E8F0', linewidth=0.8)

            # Bullet points
            bullet_y = cy + ch - 0.94
            for bullet in card["bullets"]:
                # Draw small colored dot
                dot = patches.Circle((cx + 0.32, bullet_y), 0.05, facecolor=col["color"], edgecolor='none')
                ax.add_patch(dot)

                # Word wrap manual or formatted
                # For long bullets, format nicely across 2 lines if needed
                if len(bullet) > 42:
                    # split around word boundary
                    words = bullet.split()
                    mid = len(words) // 2
                    line1 = " ".join(words[:mid])
                    line2 = " ".join(words[mid:])
                    ax.text(cx + 0.45, bullet_y + 0.08, line1, ha='left', va='center', color='#334155', fontsize=6.8, weight='medium')
                    ax.text(cx + 0.45, bullet_y - 0.16, line2, ha='left', va='center', color='#334155', fontsize=6.8, weight='medium')
                    bullet_y -= 0.45
                else:
                    ax.text(cx + 0.45, bullet_y, bullet, ha='left', va='center', color='#334155', fontsize=6.8, weight='medium')
                    bullet_y -= 0.36

    # ----------------------------------------------------
    # CONNECTING PROCESS ARROWS BETWEEN COLUMNS
    # ----------------------------------------------------
    arrow_props = dict(boxstyle="rarrow,pad=0.2", fc="#0284C7", ec="#0369A1", lw=1.2)
    arrow_positions = [5.08, 9.73, 14.38]
    for ax_pos in arrow_positions:
        arrow_box = patches.FancyBboxPatch(
            (ax_pos - 0.18, 4.85), 0.36, 0.45,
            boxstyle="round,pad=0.0,rounding_size=0.08",
            facecolor='#0284C7',
            edgecolor='#0369A1',
            linewidth=1.0
        )
        ax.add_patch(arrow_box)
        ax.text(ax_pos, 5.075, "➔", ha='center', va='center', color='#FFFFFF', fontsize=11, weight='bold')

    # Bottom Footer Summary Ribbon
    footer_ribbon = patches.FancyBboxPatch(
        (0.65, 0.45), 18.7, 0.22,
        boxstyle="round,pad=0.0,rounding_size=0.05",
        facecolor='#1E293B',
        edgecolor='none'
    )
    ax.add_patch(footer_ribbon)
    ax.text(
        10.0, 0.56,
        "CORE CONTRIBUTION: Bridging the macro-micro gap through 32-year multi-district data, unsupervised climatic zoning (k=3), non-linear ensemble classification (RF Acc: 63.63%, AUC: 0.8168), and linear regularized baselines.",
        ha='center', va='center', color='#93C5FD', fontsize=7.2, weight='semibold'
    )

    plt.tight_layout()

    # Save to candidate locations
    output_dirs = [
        r"c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment\Sukriti_Sapkota_260180_LaTeX\output_image",
        r"c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment\Assignment\latex_documentation\output_image",
        r"c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment\Assignment\full_code\figures",
        r"c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment\output_image",
        r"c:\Users\Prakriti\Downloads\Sukriti_Sapkota_260180_ML_Assignment",
        r"C:\Users\Prakriti\.gemini\antigravity\brain\637e82cc-3f3a-4e8e-bde2-9c76d45482d7"
    ]

    target_filename = "problem_statement_architecture.jpg"

    saved_paths = []
    for d in output_dirs:
        os.makedirs(d, exist_ok=True)
        out_path = os.path.join(d, target_filename)
        # Save as high-quality JPG (dpi=300)
        plt.savefig(out_path, format='jpg', dpi=300, pil_kwargs={'quality': 95})
        saved_paths.append(out_path)
        print(f"Saved: {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")

    plt.close(fig)
    print("Problem statement figure successfully generated!")

if __name__ == "__main__":
    generate_problem_statement_figure()

