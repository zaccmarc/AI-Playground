public class Aluno extends Pessoa {
    private String login;
    private int totAssistido;

    public Aluno(String nome, int idade, String sexo, float experiencia, String login, int totAssistido) {
        super(nome, idade, sexo, experiencia);
        this.login = login;
        this.totAssistido = totAssistido;
    }

    public void viuMaisUm() {
        this.totAssistido++;
        this.setExperiencia(this.getExperiencia() + 1);
    }

    public String getLogin() {
        return this.login;
    }

    public int getTotAssistido() {
        return this.totAssistido;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public void setTotAssistido(int totAssistido) {
        this.totAssistido = totAssistido;
    }

    @Override
    protected void ganharExp(float xp) {
        this.experiencia += xp;
    }
}