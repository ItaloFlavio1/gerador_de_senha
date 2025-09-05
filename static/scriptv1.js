document.addEventListener("DOMContentLoaded", () => {
    const resultadoEl = document.getElementById("senha-resultado");
    const comprimentoEl = document.getElementById("comprimento");
    const comprimentoValorEl = document.getElementById("comprimento-valor");
    const btnCopiar = document.getElementById("btn-copiar");
    const toastEl = document.getElementById("toast-copia");

    if (comprimentoEl && comprimentoValorEl) {
        comprimentoEl.addEventListener("input", (e) => {
            comprimentoValorEl.innerText = e.target.value;
        });
    }

    if (btnCopiar && resultadoEl) {
        btnCopiar.addEventListener("click", () => {
            const senha = resultadoEl.value;
            if (!senha) return;

            navigator.clipboard.writeText(senha)
                .then(() => {
                    toastEl.classList.add("show");
                    setTimeout(() => toastEl.classList.remove("show"), 2000);
                })
                .catch(err => console.error("Erro ao copiar senha:", err));
        });
    }
});
