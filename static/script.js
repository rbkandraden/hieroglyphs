// Função para exibir ou ocultar o significado do hieróglifo
document.querySelectorAll('.flashcard').forEach(card => {
    card.addEventListener('click', () => {
        const meaning = card.querySelector('.meaning');
        meaning.style.display = meaning.style.display === 'none' ? 'block' : 'none';
    });
});