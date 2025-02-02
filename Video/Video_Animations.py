from manim import *
from Manim_Functions import set_defaults

config.background_color = "#d9cdb6"

# DARKER: #1993C8 #A28F02 #627E26 #7C2927 #8C4103
# BLUE: #5BC0EB YELLOW: #FEE20B GREEN: #9BC53D RED: #C3423F ORANGE: #F17105
# LIGHTER: #B6E3F6 #FEED72 #C6DE91 #D88483 #FCA65F

# New Color Scheme
# DARK BLUE: #1B264F
# BLUE: #007991
# LIGHT BLUE: #0E9594
# RED: #D62828
# BLACK #21201E


class Animation1TitleMotivationObjective(Scene):
    def construct(self):
        b_plane = set_defaults()
        title = Text("IntrEEGing NEURONets", font_size=60, t2c={'EEG': "#D62828", 'NEURO': "#D62828"})
        title_border = SurroundingRectangle(title, buff=1.3, stroke_width=10, fill_opacity=0.5)
        by_text = Text("Created by Lauren Yu, Jonathan Mak, Ian Rundle, and Ben Allen", font_size=45) \
            .next_to(title, 11 * DOWN).scale(0.60)
        datathon_text = Text("Rice Datathon 2025").next_to(title, 11 * UP)
        vertices = [1,2,3,4,5,6]
        edges = [(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6)]
        dec_graph = Graph(vertices, edges, layout="shell", layout_scale=3,
                          vertex_config={"fill_color": "#007991", "color": "#1B264F", "stroke_opacity": 1,
                                         "stroke_width": 3},
                          edge_config={"stroke_opacity": 0.25, "color": "#21201E", "stroke_width": 5})
        dec_graph2 = dec_graph.copy().next_to(dec_graph, LEFT, buff=-0.15)
        dec_graph3 = dec_graph.copy().next_to(dec_graph, RIGHT, buff=-0.15)
        self.add(b_plane, dec_graph, dec_graph2, dec_graph3, title_border, title, by_text, datathon_text)
        self.play(DrawBorderThenFill(b_plane), DrawBorderThenFill(dec_graph), DrawBorderThenFill(dec_graph2),
                  DrawBorderThenFill(dec_graph3),
                  AnimationGroup(Write(title), DrawBorderThenFill(title_border), Write(datathon_text), Write(by_text),
                                 lag_ratio=0.4))
        self.wait(1)
        bg_title = Text("Background", font_size=50).shift(2.5 * UP)
        bg_title_border = SurroundingRectangle(bg_title, buff=0.25, stroke_width=10, fill_opacity=0.5)
        self.play(FadeOut(dec_graph, shift=DOWN), FadeOut(datathon_text, shift=UP), dec_graph2.animate.shift(2.5*LEFT),
                  dec_graph3.animate.shift(2.5*RIGHT), ReplacementTransform(title, bg_title),
                  ReplacementTransform(title_border, bg_title_border), FadeOut(by_text, shift=DOWN))

        # Motivation
        motivation_text = Paragraph("-- Mental health contributes to ~14.3% deaths worldwide",
                                    "-- Accurate, early identification is invaluable in treatment",
                                    "-- Electroencephalogram (EEG) analysis has shown promise",
                                    t2c={"Electroencephalogram (EEG)": "#D62828", "~14.3%": "#D62828"},
                                    font_size=35).shift(DOWN)
        background_text = Paragraph("-- EEGs record brainwave activity over time",
                                    "-- Measure electrical changes of neurons",
                                    "-- Electrodes located at specific places on patient's head",
                                    t2c={"EEG": "#D62828", "Electrodes": "#D62828"}, font_size=35).shift(DOWN)
        self.wait(1)
        self.play(Write(motivation_text, run_time=2))
        self.wait(1)
        self.play(Transform(motivation_text, background_text))
        self.wait(1)

        # Objectives
        ob_title = Text("Objectives", font_size=50).shift(2.5 * UP)
        ob_title_border = SurroundingRectangle(ob_title, buff=0.25, stroke_width=10, fill_opacity=0.5)
        ob_text = Paragraph("-- Create a classification model for mental disorders",
                            "-- Understand how EEGs can signal different disorders",
                            "-- Determine which disorders can be effectively modeled",
                            t2c={"classification model": "#D62828", "which disorders": "#D62828"},
                            font_size=35).shift(DOWN)
        self.play(FadeOut(motivation_text, shift=DOWN), ReplacementTransform(bg_title, ob_title),
                  ReplacementTransform(bg_title_border, ob_title_border))
        self.wait(1)
        self.play(Write(ob_text))
        self.wait(2)
        self.play(Unwrite(dec_graph2), Unwrite(dec_graph3), FadeOut(ob_title, ob_title_border, shift=2*UP),
                  Unwrite(ob_text))
        self.wait(2)


class Animation4DataDescription(Scene):
    def construct(self):
        b_plane = set_defaults()
        # Include basic size and column descriptors, but it would be cool to include a nice visual description of
        # where each EEG column is and demonstrate what PSD and COH are visually (will try using a graph for this)
        # Basic Description
        title = Text("Data Description", font_size=50).shift(2.5*UP)
        title_border = SurroundingRectangle(title, buff=0.25, stroke_width=10, fill_opacity=0.5)
        data_desc_para = Paragraph("-- 945 patients with 1148 attributes",
                                   "-- Columns covering age, sex, IQ, and education level",
                                   "-- Power spectral density (PSD) and Coherence readings",
                                   t2c={"945": "#1B264F", "1148": "#1B264F",
                                        "age": "#1B264F", "sex": "#1B264F", "IQ": "#1B264F",
                                        "education level": "#1B264F",
                                        "Power spectral density (PSD)": "#D62828", "Coherence": "#D62828"},
                                   font_size=40).scale(0.95)
        psd_text = Text("Power spectral density (PSD)").shift(3.5*UP)
        self.add(b_plane)
        self.play(DrawBorderThenFill(title_border), Write(title), Write(data_desc_para, run_time=3))
        self.wait(2)
        self.play(ReplacementTransform(data_desc_para, psd_text), FadeOut(title, title_border, shift=4*LEFT))
        self.wait(1)

        # Visual EEG Explanation
        brain = Ellipse(width=3, height=4, stroke_width=10, stroke_color="#D62828", fill_color="#DF5353",
                        fill_opacity=0.5).scale(1.15)
        ear_left = Circle(radius=0.5, stroke_width=10, stroke_color="#D62828", fill_color="#DF5353", fill_opacity=0.5)\
            .next_to(brain, LEFT, buff=0)
        ear_right = Circle(radius=0.5, stroke_width=10, stroke_color="#D62828", fill_color="#DF5353", fill_opacity=0.5)\
            .next_to(brain, RIGHT, buff=0)
        eeg_verts = ["Fp1", "Fp2", "Fz", "Cz", "Pz", "F3", "C3", "P3", "O1", "F4", "C4", "P4", "02", "F7",
                     "T3", "T5", "F8", "T4", "T6", "A1", "A2"]
        eeg_edges = [(eeg_verts[idx], eeg_verts[j]) for idx in range(len(eeg_verts)) for j in range(idx+1, len(eeg_verts))]
        mix_graph = Graph(vertices=eeg_verts,
                          edges=eeg_edges,
                          vertex_config={"fill_color": "#fff0d5", "color": "#1B264F", "stroke_opacity": 1,
                                         "stroke_width": 2, "radius": 0.475},
                          edge_config={"stroke_opacity": 0.2, "color": "#21201E", "stroke_width": 3},
                          layout="circular",
                          labels=True).scale(0.5)
        eeg_graph = Graph(vertices=eeg_verts,
                          edges=eeg_edges,
                          vertex_config={"fill_color": "#fff0d5", "color": "#1B264F", "stroke_opacity": 1,
                                         "stroke_width": 2, "radius": 0.475},
                          edge_config={"stroke_opacity": 0.2, "color": "#21201E", "stroke_width": 3},
                          layout={"Fp1": [1,3.8,0], "Fp2": [-1,3.8,0], "Fz": [0,2,0], "Cz": [0,0,0], "Pz": [0,-2,0],
                                  "F3": [1.30,2,0], "C3": [1.9,0,0], "P3": [-1.30,-2,0], "O1": [1,-3.8,0], "F4": [-1.30,2,0],
                                  "C4": [-1.9,0,0], "P4": [1.30,-2,0], "02": [-1,-3.8,0], "F7": [2.30,2.6,0], "T3": [3,0,0],
                                  "T5": [2.3,-2.6,0], "F8": [-2.3,2.6,0], "T4": [-3,0,0], "T6": [-2.3,-2.6,0],
                                  "A1": [4.5,0,0], "A2": [-4.5,0,0]},
                          labels=True).scale(0.5)
        brain_text = Text("Brain", font_size=40).move_to(brain)
        nasion_text = Text("Nasion", font_size=40).next_to(brain, UP).scale(0.75)
        inion_text = Text("Inion", font_size=40).next_to(brain, DOWN).scale(0.75)

        self.wait(1)
        self.play(AnimationGroup(DrawBorderThenFill(brain), Write(brain_text), DrawBorderThenFill(ear_left),
                                 DrawBorderThenFill(ear_right), Write(nasion_text), Write(inion_text),
                                 Write(mix_graph), lag_ratio=0.2))
        self.wait(1)
        self.play(ReplacementTransform(mix_graph, eeg_graph, run_time=2))
        self.wait(1)

        # Display concept of power spectrum density
        bands_table = Table([["Delta", "0.5–4 Hz"],
                             ["Theta", "4–7 Hz"],
                             ["Alpha", "8–13 Hz"],
                             ["Beta", "13–30 Hz"],
                             ["Gamma", "30–80 Hz"],
                             ["High Gamma", "80–150 Hz"]],
                            col_labels=[Text("Band"), Text("Frequencies")]).scale(0.5)
        bands_table.add_highlighted_cell((1, 1), color=GREEN)
        bands_table.add_highlighted_cell((1, 2), color="#1B264F")
        bands_table_border = SurroundingRectangle(bands_table, buff=0, fill_opacity=0.15, stroke_color="#21201E")
        bands_table_source = Paragraph("Source: Nayak CS, Anilkumar AC. EEG Normal Waveforms.",
                                       "[Updated 2023 Jul 24]. In: StatPearls [Internet].",
                                       "Treasure Island (FL): StatPearls Publishing; 2025 Jan-.",
                                       "Available from: https://www.ncbi.nlm.nih.gov/books/NBK539805/")\
            .scale(0.3).next_to(bands_table, DOWN, buff=0.2)
        main_table_border = SurroundingRectangle(VGroup(bands_table_border, bands_table_source),
                                                 stroke_width=10, fill_opacity=0.75)
        bands_table_group = VGroup(main_table_border, bands_table, bands_table_border, bands_table_source)\
            .move_to(ORIGIN)
        eeg_psd_graph = Graph(vertices=eeg_verts,
                              edges=eeg_edges,
                              vertex_config={"fill_color": YELLOW, "color": "#1B264F", "stroke_opacity": 1,
                                             "stroke_width": 2, "radius": 0.475},
                              edge_config={"stroke_opacity": 0.2, "color": "#21201E", "stroke_width": 3},
                              layout={"Fp1": [1, 3.8, 0], "Fp2": [-1, 3.8, 0], "Fz": [0, 2, 0], "Cz": [0, 0, 0],
                                      "Pz": [0, -2, 0],
                                      "F3": [1.30, 2, 0], "C3": [1.9, 0, 0], "P3": [-1.30, -2, 0], "O1": [1, -3.8, 0],
                                      "F4": [-1.30, 2, 0],
                                      "C4": [-1.9, 0, 0], "P4": [1.30, -2, 0], "02": [-1, -3.8, 0], "F7": [2.30, 2.6, 0],
                                      "T3": [3, 0, 0],
                                      "T5": [2.3, -2.6, 0], "F8": [-2.3, 2.6, 0], "T4": [-3, 0, 0], "T6": [-2.3, -2.6, 0],
                                      "A1": [4.5, 0, 0], "A2": [-4.5, 0, 0]},
                              labels=True).scale(0.5)
        psd_explain_text1 = Text("Measures Strength of Band", font_size=40).next_to(bands_table_group, DOWN)
        psd_explain_text2 = Text("Measured by Electrode", font_size=40).next_to(bands_table_group, DOWN)
        self.play(FadeIn(psd_explain_text1, shift=UP))
        self.wait(1)
        self.play(Write(bands_table_group), run_time=1.5)
        self.wait(2)
        self.play(Uncreate(bands_table_group), ReplacementTransform(psd_explain_text1, psd_explain_text2))
        self.wait(1)
        self.play(ReplacementTransform(eeg_graph, eeg_psd_graph))
        self.wait(1)
        self.play(FadeOut(psd_explain_text2, shift=DOWN))
        self.wait(1)

        # Display what coherence is
        coh_text = Text("Coherence").move_to(psd_text)
        coh_explain_text1 = Text("Synchronization Between Signals").move_to(psd_explain_text1)
        coh_explain_text2 = Text("Measured by Edge").move_to(psd_explain_text1)
        eeg_coh_graph = Graph(vertices=eeg_verts,
                              edges=eeg_edges,
                              vertex_config={"fill_color": "#fff0d5", "color": "#1B264F", "stroke_opacity": 1,
                                             "stroke_width": 2, "radius": 0.475},
                              edge_config={"stroke_opacity": 0.2, "color": YELLOW, "stroke_width": 3},
                              layout={"Fp1": [1, 3.8, 0], "Fp2": [-1, 3.8, 0], "Fz": [0, 2, 0], "Cz": [0, 0, 0],
                                      "Pz": [0, -2, 0],
                                      "F3": [1.30, 2, 0], "C3": [1.9, 0, 0], "P3": [-1.30, -2, 0], "O1": [1, -3.8, 0],
                                      "F4": [-1.30, 2, 0],
                                      "C4": [-1.9, 0, 0], "P4": [1.30, -2, 0], "02": [-1, -3.8, 0],
                                      "F7": [2.30, 2.6, 0],
                                      "T3": [3, 0, 0],
                                      "T5": [2.3, -2.6, 0], "F8": [-2.3, 2.6, 0], "T4": [-3, 0, 0],
                                      "T6": [-2.3, -2.6, 0],
                                      "A1": [4.5, 0, 0], "A2": [-4.5, 0, 0]},
                              labels=True).scale(0.5)
        self.play(ReplacementTransform(psd_text, coh_text), FadeIn(coh_explain_text1, shift=UP))
        self.wait(1)
        self.play(ReplacementTransform(coh_explain_text1, coh_explain_text2),
                  ReplacementTransform(eeg_psd_graph, eeg_coh_graph))
        self.wait(2)
        self.play(Unwrite(eeg_coh_graph), FadeOut(coh_text, shift=UP), FadeOut(coh_explain_text2, shift=DOWN),
                  Unwrite(nasion_text), Unwrite(inion_text), Unwrite(brain_text), Uncreate(brain), Uncreate(ear_left),
                  Uncreate(ear_right))
        self.wait(1)


class Animation5DataCleaningFeatureEngineering(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        vertices = [1,2,3,4,5,6]
        edges = [(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6)]
        dec_graph = Graph(vertices, edges, layout="shell", layout_scale=3,
                          vertex_config={"fill_color": "#007991", "color": "#1B264F", "stroke_opacity": 0.25,
                                         "stroke_width": 3, "fill_opacity": 0.25},
                          edge_config={"stroke_opacity": 0.25, "color": "#21201E", "stroke_width": 5})
        dec_graph2 = dec_graph.copy().next_to(dec_graph, LEFT, buff=-0.15)
        dec_graph3 = dec_graph.copy().next_to(dec_graph, RIGHT, buff=-0.15)

        # Dropped rows with missing data, normalization, etc.
        dc_title = Text("Data Cleaning", font_size=50).shift(2.5 * UP)
        dc_title_border = SurroundingRectangle(dc_title, buff=0.25, stroke_width=10, fill_opacity=0.5)
        dc_text = Paragraph("1. Dropped 24 Rows Containing NA Values",
                            "2. Dropped Non EEG Related Columns",  # Difficult to work with
                            "3. Standardized EEG Data",
                            t2c={"24": "#D62828", "NA": "#D62828", "Non": "#D62828", "Standardized": "#007991"},
                            font_size=40).shift(DOWN)

        # Feature Engineering
        # SMOTE, PCA, etc. (can include mathematical/visual descriptions of these methods)
        fe_title = Text("Feature Engineering", font_size=50).shift(2.5 * UP)
        fe_title_border = SurroundingRectangle(fe_title, buff=0.25, stroke_width=10, fill_opacity=0.5)
        fe_text = Paragraph("1. Parsed Electrodes to Construct Graph for GNN",
                            "2. Attempted Dimensionality Reduction (PCA, UMAP)",
                            "3. Attempted to Use SMOTE to Address Class Imbalance",
                            t2c={"Adjacency Matrix": "#D62828", "PCA": "#1B264F", "UMAP": "#1B264F", "SMOTE": "#1B264F"},
                            font_size=37).shift(DOWN)

        """self.play(Write(VGroup(dec_graph2, dec_graph, dec_graph3)), Create(dc_title_border), Write(dc_title))
        self.wait(1)
        self.play(Write(dc_text))
        self.wait(1)
        self.play(FadeOut(dc_text, shift=DOWN))
        self.wait(1)
        self.play(Transform(dc_title_border, fe_title_border), Transform(dc_title, fe_title))
        self.wait(1)
        self.play(Write(fe_text))
        self.wait(1)"""

        # Can add more here explaining the adjacency matrix stuff
        adj_title = Text("Constructing Graph", font_size=50).shift(3 * UP)
        adj_title_border = SurroundingRectangle(adj_title, buff=0.25, stroke_width=10, fill_opacity=0.5)
        adj_step1_text = Text("1. Find maximum coherence across bands", font_size=40).shift(3*DOWN)
        adj_step2_text = Text("2. Set max coherence as weight and keep top 10", font_size=40).shift(3*DOWN)
        adj_step3_text = Text("3. Construct graph using pytorch-geometric", font_size=40).shift(3*DOWN)
        adj_explain_text = Text("Coherence is used to understand structure of brain", font_size=40).shift(3*DOWN)
        brain = Ellipse(width=3, height=4, stroke_width=10, stroke_color="#D62828", fill_color="#DF5353",
                        fill_opacity=0.5).scale(1.15)
        ear_left = Circle(radius=0.5, stroke_width=10, stroke_color="#D62828", fill_color="#DF5353", fill_opacity=0.5) \
            .next_to(brain, LEFT, buff=0)
        ear_right = Circle(radius=0.5, stroke_width=10, stroke_color="#D62828", fill_color="#DF5353", fill_opacity=0.5) \
            .next_to(brain, RIGHT, buff=0)
        eeg_verts = ["Fp1", "Fp2", "Fz", "Cz", "Pz", "F3", "C3", "P3", "O1", "F4", "C4", "P4", "02", "F7",
                     "T3", "T5", "F8", "T4", "T6", "A1", "A2"]
        eeg_edges = [(eeg_verts[idx], eeg_verts[j]) for idx in range(len(eeg_verts)) for j in
                     range(idx + 1, len(eeg_verts))]
        mix_graph = Graph(vertices=eeg_verts,
                          edges=eeg_edges,
                          vertex_config={"fill_color": "#fff0d5", "color": "#1B264F", "stroke_opacity": 1,
                                         "stroke_width": 2, "radius": 0.475},
                          edge_config={"stroke_opacity": 0.2, "color": "#21201E", "stroke_width": 3},
                          layout="circular",
                          labels=True).scale(0.5)
        eeg_graph = Graph(vertices=eeg_verts,
                          edges=eeg_edges,
                          vertex_config={"fill_color": "#fff0d5", "color": "#1B264F", "stroke_opacity": 1,
                                         "stroke_width": 2, "radius": 0.475},
                          edge_config={"stroke_opacity": 0.2, "color": "#21201E", "stroke_width": 3},
                          layout={"Fp1": [1, 3.8, 0], "Fp2": [-1, 3.8, 0], "Fz": [0, 2, 0], "Cz": [0, 0, 0],
                                  "Pz": [0, -2, 0],
                                  "F3": [1.30, 2, 0], "C3": [1.9, 0, 0], "P3": [-1.30, -2, 0], "O1": [1, -3.8, 0],
                                  "F4": [-1.30, 2, 0],
                                  "C4": [-1.9, 0, 0], "P4": [1.30, -2, 0], "02": [-1, -3.8, 0], "F7": [2.30, 2.6, 0],
                                  "T3": [3, 0, 0],
                                  "T5": [2.3, -2.6, 0], "F8": [-2.3, 2.6, 0], "T4": [-3, 0, 0], "T6": [-2.3, -2.6, 0],
                                  "A1": [4.5, 0, 0], "A2": [-4.5, 0, 0]},
                          labels=True).scale(0.5)
        VGroup(eeg_graph, mix_graph, brain, ear_right, ear_left).shift(3*LEFT+0.5*DOWN)
        bands_table = Table([["Delta", "80 COH"],
                             ["Theta", "60 COH"],
                             ["Alpha", "30 COH"],
                             ["Beta", "100 COH"],
                             ["Gamma", "50 COH"],
                             ["High Gamma", "35 COH"]],
                            col_labels=[Text("Band"), Text("Fp1-Fp2 Coherence")]).scale(0.4)
        bands_table.add_highlighted_cell((1, 1), color=GREEN)
        bands_table.add_highlighted_cell((1, 2), color="#1B264F")
        bands_table_border = SurroundingRectangle(bands_table, buff=0, fill_opacity=0.15, stroke_color="#21201E")
        main_table_border = SurroundingRectangle(bands_table_border, stroke_width=10, fill_opacity=0.75)
        bands_table_group = VGroup(main_table_border, bands_table, bands_table_border)\
            .next_to(ear_right, RIGHT, buff=0.5)
        pytorch_text = Paragraph("Pytorch-Geometric",
                                 "Graph", fontsize=50).move_to(bands_table_group)
        pytorch_border = SurroundingRectangle(pytorch_text, stroke_width=10, fill_opacity=0.75)
        pytorch_arrow = Arrow(start=ear_right.get_right(), end=pytorch_border.get_left())
        self.play(Transform(dc_title_border, adj_title_border), Transform(dc_title, adj_title))
        self.wait(1)
        self.play(AnimationGroup(DrawBorderThenFill(brain), DrawBorderThenFill(ear_left),
                                 DrawBorderThenFill(ear_right), Write(mix_graph), lag_ratio=0.2))
        self.wait(1)
        self.play(ReplacementTransform(mix_graph, eeg_graph, run_time=0.75), Write(bands_table_group))
        self.wait(1)
        self.play(Write(adj_step1_text))
        weight_label = MathTex("100 COH", font_size=30, color="#0E9594")\
            .next_to(eeg_graph.edges[("Fp1", "Fp2")], UP, buff=0.2)
        self.play(Write(weight_label), eeg_graph.edges[("Fp1", "Fp2")].animate.set_opacity(1))
        self.wait(1)
        self.play(ReplacementTransform(adj_step1_text, adj_step2_text),
                  AnimationGroup(eeg_graph.edges[("Fp1", "Fp2")].animate.set_color(YELLOW).set_opacity(1),
                                 eeg_graph.edges[("Fp1", "Fz")].animate.set_color(YELLOW).set_opacity(1),
                                 eeg_graph.edges[("Fp1", "Cz")].animate.set_color(YELLOW).set_opacity(1),
                                 eeg_graph.edges[("Fp1", "F3")].animate.set_color(YELLOW).set_opacity(1),
                                 eeg_graph.edges[("Fp1", "P4")].animate.set_color(YELLOW).set_opacity(1),
                                 eeg_graph.edges[("Fp1", "T5")].animate.set_color(YELLOW).set_opacity(1),
                                 eeg_graph.edges[("Fp1", "T3")].animate.set_color(YELLOW).set_opacity(1),
                                 eeg_graph.edges[("Fp1", "F7")].animate.set_color(YELLOW).set_opacity(1),
                                 eeg_graph.edges[("Fp1", "F4")].animate.set_color(YELLOW).set_opacity(1),
                                 eeg_graph.edges[("Fp1", "F8")].animate.set_color(YELLOW).set_opacity(1),
                                 lag_ratio=0.2))
        self.wait(1)
        self.play(ReplacementTransform(adj_step2_text, adj_step3_text),
                  ReplacementTransform(bands_table_group, VGroup(pytorch_border, pytorch_text)),
                  DrawBorderThenFill(pytorch_arrow))
        self.wait(1)
        self.play(ReplacementTransform(adj_step3_text, adj_explain_text))
        self.wait(1)


class SimpleGraph(Scene):
    def construct(self):
        # Define the graph with nodes and edges
        vertices = ["Fp1", "Fp2"]  # Nodes
        edges = [("Fp1", "Fp2")]   # Edge connecting Fp1 and Fp2

        # Create the graph
        graph = Graph(vertices, edges, layout="circular")

        # Customize the appearance of the graph
        graph["Fp1"].set_color(BLUE)  # Set color of Fp1 node
        graph["Fp2"].set_color(RED)   # Set color of Fp2 node
        graph.edges[("Fp1", "Fp2")].set_color(GREEN)  # Set color of the edge

        # Add the graph to the scene
        self.play(Create(graph))
        self.wait(2)  # Wait for 2 seconds to display the graph


class Animation7Modeling(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        model_text = Text("Full Model Architecture", font_size=50, color="#FEE20B") \
            .shift(3.5 * UP)
        df1_text = Paragraph("Preprocessed", "Dataframe", font_size=35)
        df2_text = Paragraph("Standardized", "Dataframe", font_size=35)
        dfs_group = VGroup(df2_text, df1_text).arrange(buff=2).shift(2 * UP)
        df1_box = SurroundingRectangle(df1_text, stroke_color="#C3423F", fill_color="#C3423F")
        df2_box = SurroundingRectangle(df2_text, stroke_color="#C3423F", fill_color="#C3423F")
        xg1_text = Paragraph("General", "XGBoost", font_size=35).scale(0.75)
        xg2_text = Paragraph("Small-Value", "XGBoost", font_size=35).scale(0.75)
        xg3_text = Paragraph("Large-Value", "XGBoost", font_size=35).scale(0.75)
        xg4_text = Paragraph("Extreme-Value", "XGBoost", font_size=35).scale(0.75)
        xg_group = VGroup(xg4_text, xg3_text, xg2_text, xg1_text).arrange(buff=0.65, direction=LEFT)
        nn_text = Paragraph("Neural", "Network", font_size=35).scale(0.75)
        model_group = VGroup(xg_group, nn_text).arrange(buff=0.85, direction=LEFT).next_to(dfs_group, DOWN) \
            .shift(1.25 * DOWN)
        xg1_box = SurroundingRectangle(xg1_text, stroke_color="#5BC0EB", fill_color="#5BC0EB")
        xg2_box = SurroundingRectangle(xg2_text, stroke_color="#5BC0EB", fill_color="#5BC0EB")
        xg3_box = SurroundingRectangle(xg3_text, stroke_color="#5BC0EB", fill_color="#5BC0EB")
        xg4_box = SurroundingRectangle(xg4_text, stroke_color="#5BC0EB", fill_color="#5BC0EB")
        nn_box = SurroundingRectangle(nn_text, stroke_color="#F17105", fill_color="#F17105")
        blend_text = Paragraph("XGBoost", "Blender", font_size=35).next_to(model_group, DOWN).shift(DOWN)
        blend_box = SurroundingRectangle(blend_text, stroke_color="#FEE20B", fill_color="#FEE20B")
        arrow1 = CurvedArrow(start_point=df1_box.get_bottom(), end_point=xg1_box.get_top(), angle=PI / 8,
                             color="#5BC0EB")
        arrow2 = CurvedArrow(start_point=df1_box.get_bottom(), end_point=xg2_box.get_top(), angle=PI / 8,
                             color="#5BC0EB")
        arrow3 = CurvedArrow(start_point=df1_box.get_bottom(), end_point=xg3_box.get_top(), angle=PI / 8,
                             color="#5BC0EB")
        arrow4 = CurvedArrow(start_point=df1_box.get_bottom(), end_point=xg4_box.get_top(), angle=PI / 8,
                             color="#5BC0EB")
        arrow5 = CurvedArrow(start_point=df2_box.get_bottom(), end_point=nn_box.get_top(), angle=PI / 8)
        arrow7 = CurvedArrow(start_point=xg1_box.get_bottom(), end_point=blend_box.get_top(), angle=PI / 8,
                             color="#FEE20B")
        arrow8 = CurvedArrow(start_point=xg2_box.get_bottom(), end_point=blend_box.get_top(), angle=PI / 8,
                             color="#FEE20B")
        arrow9 = CurvedArrow(start_point=xg3_box.get_bottom(), end_point=blend_box.get_top(), angle=-PI / 8,
                             color="#FEE20B")
        arrow10 = CurvedArrow(start_point=xg4_box.get_bottom(), end_point=blend_box.get_right(), angle=-PI / 4,
                              color="#FEE20B")
        arrow11 = CurvedArrow(start_point=nn_box.get_bottom(), end_point=blend_box.get_left(), color="#FEE20B")
        arrow_group = VGroup(arrow1, arrow2, arrow3, arrow4,
                             arrow5, arrow7, arrow8,
                             arrow9, arrow10, arrow11)
        box_group = VGroup(blend_box, nn_box, xg1_box, xg2_box, xg3_box, xg4_box, df1_box, df2_box)
        df_highlight = SurroundingRectangle(dfs_group, buff=0.25, stroke_color="#FEE20B", fill_color="#FEE20B")
        xg_highlight = SurroundingRectangle(xg_group, buff=0.25, stroke_color="#FEE20B", fill_color="#FEE20B")
        nn_highlight = SurroundingRectangle(nn_text, stroke_color="#FEE20B", fill_color="#FEE20B", buff=0.25)
        df_info_rect = Rectangle(stroke_color="#fff0d5", fill_color="#211A1E", fill_opacity=0.85, height=7,
                                 width=4).shift(5 * RIGHT)
        df1_title = Text("Preprocessed").next_to(df_info_rect.get_top(), DOWN).scale(0.75)
        df1_info = Paragraph("- MICE Imputation",
                             "- One-Hot Encoding",
                             "- Horizontal Dist. Var.",
                             "- Outliers Removed",
                             line_spacing=2).next_to(df1_title, DOWN).scale(0.5)
        df2_title = Text("Standardized").next_to(df_info_rect.get_top(), DOWN).scale(0.75)
        df2_info = Paragraph("- Used TensorFlow",
                             "- Gaussian Proximity",
                             "- Horizontal Dist. Var.",
                             "- Normalized Data",
                             line_spacing=2).next_to(df2_title, DOWN).scale(0.5)
        self.play(Write(model_text), Write(box_group), Write(dfs_group), Write(model_group), Write(blend_text),
                  Write(arrow_group))
        self.wait(3)
        self.play(DrawBorderThenFill(df_highlight))
        self.wait(1)
        self.play(FadeIn(df_info_rect, df1_info, df1_title, shift=LEFT))
        self.wait(1)
        self.play(ReplacementTransform(df1_info, df2_info), ReplacementTransform(df1_title, df2_title))
        self.wait(1)
        self.play(FadeOut(df_info_rect, df2_info, df2_title, shift=RIGHT))
        self.wait(1)
        self.play(DrawBorderThenFill(xg_highlight), Unwrite(df_highlight))
        self.wait(1)
        self.play(DrawBorderThenFill(nn_highlight), Unwrite(xg_highlight))
        self.wait(1)
        self.play(Unwrite(model_text, run_time=1), Unwrite(box_group, run_time=1),
                  Unwrite(dfs_group, run_time=1), Unwrite(model_group, run_time=1),
                  Unwrite(blend_text, run_time=1), Unwrite(arrow_group, run_time=1),
                  Unwrite(nn_highlight, run_time=1))
        self.wait(1)


class Animation8Evaluation(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        accuracy_text = Text("Accuracy")
        precision_text = Text("Precision")
        recall_text = Text("Recall")
        f1_text = Text("F1 Score")
        formula_titles = VGroup(accuracy_text, precision_text, recall_text, f1_text).arrange_in_grid(rows=2, buff=2)
        accuracy_formula = MathTex("\\frac{TP+TN}{TP+TN+FP+FN}").next_to(accuracy_text, DOWN)
        precision_formula = MathTex("\\frac{TP}{TP+FP}").next_to(precision_text, DOWN)
        recall_formula = MathTex("\\frac{TP}{TP+FN}").next_to(recall_text, DOWN)
        f1_formula = MathTex("\\frac{2\\cdot Precision\\cdot Recall}{Precision+Recall}").next_to(f1_text, DOWN)
        formulas = VGroup(accuracy_formula, precision_formula, recall_formula, f1_formula)
        eval_title = Text("Feature Engineering", font_size=50).shift(2.5 * UP)
        eval_title_border = SurroundingRectangle(eval_title, buff=0.25, stroke_width=10, fill_opacity=0.5)
        # Describe how model was evaluated (can be skipped for time) and how the model did (accuracy, precision, recall,
        # and most importantly confusion matrix)
        self.add(formula_titles, formulas, eval_title, eval_title_border)


class Animation9InsightsConclusion(Scene):
    def construct(self):
        b_plane = set_defaults()
        self.add(b_plane)
        # Include any cool visualizations here can move these up if they help explain any of the preprocessing or
        # modeling steps we took
        # Standard conclusion side with key takeaways and a thank you (mention organizers and neurotech specifically)
        # Insights
        # 1st Insight - PSD Graph from Lauren
        insight_graph = ImageMobject("Visualizations/PSD.png").scale(0.9)
        insight_graph_border = SurroundingRectangle(insight_graph, buff=0.075, stroke_width=10, fill_opacity=0.75,
                                                    stroke_color=["#D62828", "#0E9594", "#1B264F", "#F17105"])
        insight_graph_border2 = SurroundingRectangle(insight_graph, buff=0.4, stroke_width=11, fill_opacity=0.5,
                                                     stroke_color=["#D62828", "#0E9594", "#1B264F", "#F17105"],
                                                     fill_color=["#D62828", "#0E9594", "#1B264F", "#F17105"])
        pointer_dot = Dot(radius=0.1, color=RED).shift(2.33*RIGHT+2.3*UP)
        pointer_dot2 = Dot(radius=0.1, color=RED).shift(2.22 * LEFT + 2.3 * UP)
        pointer_dot3 = Dot(radius=0.1, color=RED).shift(3.512 * LEFT + 2.3 * UP)
        pointer_dot4 = Dot(radius=0.1, color=RED).shift(1.68 * RIGHT + 1 * DOWN)
        pointer_image = ImageMobject("Visualizations/PSD_Part1.png").move_to(pointer_dot).scale(1.25)\
            .shift(0.5*LEFT+1.5*DOWN)
        pointer_image2 = ImageMobject("Visualizations/PSD_Part2.png").move_to(pointer_dot2).scale(1.25)\
            .shift(0.5*RIGHT+1.5*DOWN)
        pointer_image3 = ImageMobject("Visualizations/PSD_Part3.png").move_to(pointer_dot3).scale(1.25).shift(1.5*DOWN)
        pointer_image4 = ImageMobject("Visualizations/PSD_Part4.png").move_to(pointer_dot4).scale(1.25).shift(1.5*DOWN)
        pointer_border = SurroundingRectangle(pointer_image, buff=0, stroke_width=6, fill_opacity=0.9,
                                              stroke_color="#1B264F", fill_color="#fff0d5")
        pointer_border2 = SurroundingRectangle(pointer_image2, buff=0, stroke_width=6, fill_opacity=0.9,
                                               stroke_color="#1B264F", fill_color="#fff0d5")
        pointer_border3 = SurroundingRectangle(pointer_image3, buff=0, stroke_width=6, fill_opacity=0.9,
                                               stroke_color="#1B264F", fill_color="#fff0d5")
        pointer_border4 = SurroundingRectangle(pointer_image4, buff=0, stroke_width=6, fill_opacity=0.9,
                                               stroke_color="#1B264F", fill_color="#fff0d5")
        pointer_arrow = CurvedArrow(start_point=pointer_border.get_top(), end_point=pointer_dot.get_center(),
                                    stroke_color="#1B264F")
        pointer_arrow2 = CurvedArrow(start_point=pointer_border2.get_top(), end_point=pointer_dot2.get_center(),
                                     stroke_color="#1B264F")
        pointer_arrow3 = CurvedArrow(start_point=pointer_border3.get_top(), end_point=pointer_dot3.get_center(),
                                     stroke_color="#1B264F")
        pointer_arrow4 = CurvedArrow(start_point=pointer_border4.get_top(), end_point=pointer_dot4.get_center(),
                                     stroke_color="#1B264F")
        self.play(DrawBorderThenFill(insight_graph_border2), DrawBorderThenFill(insight_graph_border),
                  FadeIn(insight_graph))
        self.wait(1)
        self.play(Create(pointer_border), Create(pointer_arrow), FadeIn(pointer_image),
                  Create(pointer_border3), Create(pointer_arrow3), FadeIn(pointer_image3))
        self.wait(1)
        self.play(FadeOut(pointer_border), FadeOut(pointer_arrow), FadeOut(pointer_image),
                  FadeOut(pointer_border3), FadeOut(pointer_arrow3), FadeOut(pointer_image3))
        self.wait(1)
        self.play(Create(pointer_border2), Create(pointer_arrow2), FadeIn(pointer_image2))
        self.wait(1)
        self.play(FadeOut(pointer_border2), FadeOut(pointer_arrow2), FadeOut(pointer_image2))
        self.wait(1)
        self.play(Create(pointer_border4), Create(pointer_arrow4), FadeIn(pointer_image4))
        self.wait(1)
        self.play(FadeOut(pointer_border4), FadeOut(pointer_arrow4), FadeOut(pointer_image4))
        self.wait(1)
        self.play(Uncreate(insight_graph_border), Uncreate(insight_graph_border2), FadeOut(insight_graph))
        self.wait(1)

        # Conclusion
        results_title = Text("Conclusion", font_size=50, color="#007991").shift(2.5 * UP)
        results_text = Paragraph("Our GNN Model Achieved", "a Validation Accuracy of 94.93%!", font_size=60,
                                 t2c={"94.93%!": "#D62828", "GNN Model": "#D62828"})
        conc_border = SurroundingRectangle(results_text, buff=0.5, stroke_width=10)
        self.play(DrawBorderThenFill(results_title), Write(results_text), DrawBorderThenFill(conc_border))
        self.wait(1)
        analysis_text = Paragraph("Future Work May Look Into Adding Additional",
                                  "Features Beyond EEG Signals.",
                                  font_size=40, t2c={"vertical depth": " #1B264F", "location": " #1B264F",
                                                     "horizontal length": " #1B264F"})
        analysis_border = SurroundingRectangle(analysis_text, buff=0.5, stroke_width=10)
        self.play(ReplacementTransform(results_text, analysis_text), ReplacementTransform(conc_border, analysis_border))
        self.wait(1)

        # Thank You
        thanks_text = Paragraph("Thanks to Datathon Organizers", "and Neurotech@Rice!", font_size=60,
                                gradient=("#D62828", "#0E9594", "#1B264F", "#F17105"))
        thanks_border = SurroundingRectangle(thanks_text, buff=0.5, stroke_width=15,
                                             stroke_color=["#D62828", "#0E9594", "#1B264F", "#F17105"],
                                             fill_color=["#D62828", "#0E9594", "#1B264F", "#F17105"])
        self.play(ReplacementTransform(analysis_text, thanks_text), FadeOut(results_title, shift=UP),
                  ReplacementTransform(analysis_border, thanks_border))
        self.wait(1)
