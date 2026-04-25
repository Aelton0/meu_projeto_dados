from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np

#plot
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
    """Gera e salva um gráfico padronizado de forma segura e sem memory leaks."""

    # 1. Validação Rápida (Fail Fast)
    if x_range[0] >= x_range[1]:
        raise ValueError("O limite inferior de x_range deve ser menor que o superior.")

    # 2. Processamento Vetorizado
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = func(x)

    # 3. Criação da Figura
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    try:  # Usamos try/finally para GARANTIR a liberação de memória, mesmo se houver erro
        ax.plot(x, y, linewidth=2)

        # 4. Tratamento robusto para o nome da função (Evitando '<lambda>')
        if not title:
            func_name = getattr(func, "__name__", "customizada")
            if func_name == "<lambda>":
                title = "Gráfico de Função Anônima"
            else:
                title = f"y = {func_name}(x)"

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.3)

        # 5. Segurança de I/O: Garante que o diretório existe
        output_path = Path(filename)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        fig.savefig(output_path, bbox_inches="tight")
        print(f"Sucesso: {output_path.absolute()}")

    finally:
        # 6. O FATOR ELITE: Prevenção de Memory Leak
        plt.close(fig)


def main() -> None:
    # Teste 1: Função Lambda
    standardized_plot(
        func=lambda x: x**2,
        x_range=(-5.0, 5.0),
        title="f(x) = x²",
        filename="outputs/x2_plot.png",  # Testando a criação de diretórios
    )

    # Teste 2: Função Numpy nativa
    standardized_plot(func=np.sin, x_range=(0.0, 10.0), filename="outputs/sin_plot.png")


if __name__ == "__main__":
    main()
