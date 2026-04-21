from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


def standardized_plot(
    func: Callable[[np.ndarray], np.ndarray],
    x_range: tuple[float, float] = (0.0, 10.0),
    num_points: int = 500,
    title: str | None = None,
    xlabel: str = "x",
    ylabel: str = "y",
    filename: str = "plot.png",
    figsize: tuple[float, float] = (6.0, 4.0),
    dpi: int = 150,
) -> None:
    """
    Gera e salva um gráfico padronizado para uma dada função matemática.
    """
    x = np.linspace(x_range[0], x_range[1], num_points)  # Gerar x
    y = func(x)  # Avaliar função

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)  # Criar figura
    ax.plot(x, y, linewidth=2)

    # Título
    if title is None:
        title = f"y = {func.__name__}(x)"
    ax.set_title(title)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)

    plt.show()  # Mostrar imagem
    fig.savefig(filename, bbox_inches="tight")  # Salvar para arquivo
    print(f"Saved: {filename}")


def main() -> None:
    standardized_plot(
        func=lambda x: x**2,
        x_range=(-5.0, 5.0),
        num_points=100,
        title="f(x) = x²",
        filename="x2_plot.png",
    )

    standardized_plot(func=np.sin, x_range=(0.0, 10.0), filename="sin_plot.png")


if __name__ == "__main__":
    main()
