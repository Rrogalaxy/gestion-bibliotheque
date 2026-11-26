import logging
from pathlib import Path

import customtkinter as ctk
from PIL import Image

logger: logging.Logger = logging.getLogger(__name__)

BG_COLOR: str = "#f5efe3"
CARD_COLOR: str = "#ffffff"
LOGO_PATH: Path = Path("Capture d'écran 2025-12-03 105917.png")
LOGO_SIZE: tuple[int, int] = (80, 80)
PROFILE_COUNT: int = 5


class BiblioView(ctk.CTk):
    """
    Profile selection window of the library application.
    """

    def __init__(self) -> None:
        """
        A function that builds the window and its widgets.

        Args :
            None

        Return :
            None
        """
        super().__init__()

        # init the window
        self.title("Window")
        self.geometry("1000x500")
        self.configure(fg_color=BG_COLOR)

        self._build_header_spacer()
        self._build_logo()
        self._build_titles()
        self.profiles_frame: ctk.CTkFrame = self._build_profiles_frame()
        self.profile_cards: list[ctk.CTkFrame] = self._build_profile_cards()

    def _build_header_spacer(self) -> None:
        """
        A function that adds the empty top frame used as vertical spacing.

        Args :
            None

        Return :
            None
        """
        spacer: ctk.CTkFrame = ctk.CTkFrame(
            self, fg_color="transparent", bg_color="transparent", height=140
        )
        # keep the fixed height even though the frame is empty
        spacer.pack_propagate(False)
        spacer.pack(side="top", fill="x", expand=True)

    def _load_logo(self) -> ctk.CTkImage | None:
        """
        A function that loads the logo image from disk.

        Args :
            None

        Return :
            The logo image (CTkImage), or None if the file cannot be loaded
        """
        try:
            image: Image.Image = Image.open(LOGO_PATH)
            return ctk.CTkImage(light_image=image, dark_image=image, size=LOGO_SIZE)
        except (FileNotFoundError, OSError) as error:
            logger.error("Cannot load logo '%s': %s", LOGO_PATH, error)
            return None

    def _build_logo(self) -> None:
        """
        A function that adds the logo label (image only, no text).

        Args :
            None

        Return :
            None
        """
        logo: ctk.CTkLabel = ctk.CTkLabel(
            self,
            text="",
            image=self._load_logo(),
            bg_color="transparent",
            text_color=("#000000", "#000000"),
        )
        logo.pack(side="top", expand=True)

    def _build_titles(self) -> None:
        """
        A function that adds the title and the subtitle labels.

        Args :
            None

        Return :
            None
        """
        title: ctk.CTkLabel = ctk.CTkLabel(
            self,
            text="Qui êtes-vous ?",
            font=ctk.CTkFont(family="Arial", size=27),
            text_color=("gray10", "#000000"),
            height=40,
        )
        title.pack(side="top", expand=True)

        subtitle: ctk.CTkLabel = ctk.CTkLabel(
            self,
            text="sélectionnez votre profil pour accéder à la bibliothèque",
            font=ctk.CTkFont(family="Arial"),
            text_color=("gray10", "#000000"),
        )
        subtitle.pack(side="top", expand=True)

    def _build_profiles_frame(self) -> ctk.CTkFrame:
        """
        A function that adds the bottom container holding the profile cards.

        Args :
            None

        Return :
            The container frame (CTkFrame)
        """
        frame: ctk.CTkFrame = ctk.CTkFrame(
            self, fg_color="transparent", bg_color="transparent"
        )
        frame.pack(side="bottom", fill="x", expand=True)
        return frame

    def _build_profile_cards(self) -> list[ctk.CTkFrame]:
        """
        A function that creates the profile cards, laid out left to right.

        Args :
            None

        Return :
            The list of cards (list[CTkFrame])
        """
        cards: list[ctk.CTkFrame] = []
        for _ in range(PROFILE_COUNT):
            card: ctk.CTkFrame = ctk.CTkFrame(
                self.profiles_frame,
                width=130,
                height=170,
                corner_radius=20,
                border_width=0,
                fg_color=CARD_COLOR,
                bg_color="transparent",
            )
            card.pack(side="left", expand=True, padx=12, pady=(0, 12))
            cards.append(card)
        return cards


def main() -> None:
    """
    A function that configures the theme and starts the application.

    Args :
        None

    Return :
        None
    """
    logging.basicConfig(level=logging.INFO)
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app: BiblioView = BiblioView()
    app.mainloop()


if __name__ == "__main__":
    main()
