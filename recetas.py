import customtkinter as ctk


class RecetasMixin:
    def build_recipes_tab(self):
        self.recipes_tab = self.tabview.tab("Recetas")
        self.recipes_tab.grid_columnconfigure(0, weight=1)
        self.recipes_tab.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(self.recipes_tab, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        ctk.CTkLabel(header_frame, text="Recetas", font=ctk.CTkFont(size=20, weight="bold")).pack(side="left")
        ctk.CTkButton(header_frame, text="+ Nueva Receta", fg_color="#6366f1", hover_color="#4f46e5").pack(side="right")

        empty_frame = ctk.CTkFrame(self.recipes_tab, fg_color="#2b2b2b", corner_radius=10)
        empty_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

        ctk.CTkLabel(
            empty_frame,
            text="Todavia no hay recetas cargadas",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=(80, 8))
        ctk.CTkLabel(
            empty_frame,
            text="Esta pantalla ya esta separada para agregar el modulo de recetas.",
            text_color="gray"
        ).pack()
