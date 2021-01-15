public class Event {

    private java.sql.Timestamp ts;
    private String company;
    private Double px;

    public Event(java.sql.Timestamp ts, String company, Double px){
        this.ts = ts;
        this.company = company;
        this.px = px;
    }

    public java.sql.Timestamp getTs() {
        return ts;
    }

    public String getCompany() {
        return company;
    }

    public Double getPx() {
        return px;
    }

    @Override
    public String toString() {
        return "Event{" +
                "ts='" + ts + '\'' +
                ", company='" + company + '\'' +
                ", px=" + px +
                '}';
    }
}
