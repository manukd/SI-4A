import java.util.Random;

public class Gene {
    private int value;

    public Gene() {
        this.value = new Random().nextInt(2);
    }

    public Gene(int _value) {
        if(_value == 0 || _value == 1)
            this.value = _value;
    }

    public int getValue() {
        return this.value;
    }

    @Override
    public String toString() {
        return String.valueOf(this.getValue());
    }
}
