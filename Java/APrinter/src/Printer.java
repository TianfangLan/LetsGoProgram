public class Printer {

    private int tonerLevel;
    private int pagesPrinted;
    private boolean duplex;


    public Printer(int tonerLevel, boolean duplex) {
        if (100 < this.tonerLevel || this.tonerLevel < 0) {
            this.tonerLevel = -1;
        } else {
            this.tonerLevel = tonerLevel;
        }
        this.pagesPrinted = 0;
        this.duplex = duplex;
    }

    public int addToner(int tonerAmount) {
        if (100 < tonerAmount || tonerAmount <= 0 || tonerAmount + tonerLevel > 100 || tonerLevel == -1) {
            return -1;
        } else {
            this.tonerLevel += tonerAmount;
            return tonerLevel;
        }
    }

    public int printPages(int pageToPrint) {
        if (pageToPrint < 0 || tonerLevel == -1) {
            return -1;
        }
        if (this.duplex) {
            pageToPrint = (pageToPrint / 2) + (pageToPrint % 2);
        }
        pagesPrinted += pageToPrint;
        return pageToPrint;
    }

    public int getPagesPrinted() {
        return pagesPrinted;
    }
}
