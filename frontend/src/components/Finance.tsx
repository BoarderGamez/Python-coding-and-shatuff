import Image from 'next/image'

export default function Finance() {
  return (
    <section className="mb-6 text-center">
      <h2 className="text-2xl font-bold mb-4">Unlock Ai Waifu weather Insights</h2>

      <div className="flex justify-center items-center gap-8">
        {/* Bitcoin / OIP */}
        <div className="text-center">
          <Image src="/OIP.png" alt="OIP Icon" width={60} height={60} />
          <p className="mt-2 text-lg font-semibold">$500</p>
        </div>

        {/* EA SPORTS */}
        <div className="text-center">
          <Image src="/the_ea_sports_logo_from_1993_2000_by_mjegameandcomicfan89_dbl8vai-fullview.jpg" alt="EA SPORTS Logo" width={100} height={50} />
          <p className="mt-2 text-sm text-gray-600">EA SPORTS</p>
        </div>

        {/* Lock Icon */}
        <div className="text-center">
          <Image src="/54-546484_original-big-image-png-lock-png-transparent-png.png" alt="Lock Icon" width={50} height={50} />
          <p className="mt-2 text-sm text-gray-600">Secure</p>
        </div>
      </div>
    </section>
  )
}
